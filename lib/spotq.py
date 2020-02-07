import spotipy
import spotipy.util as util
import pprint
import os
import sys

from spotdl import youtube_tools
from spotdl import downloader
from spotdl import internals
from spotdl import const
from spotdl import handle


username = "phcreery"
scope = 'user-library-read'
token = util.prompt_for_user_token(username,scope,client_id='46508b20d6e7448dad0476c7162efffb',client_secret='2f9cefbfa0544dd38e245047217909ef',redirect_uri='http://localhost:8888/callback')

#os.system("clear")

if token:
	spotify = spotipy.Spotify(auth=token)

else:
	print("Can't get token for", username)




def savedtracks(spotify):
	results = spotify.current_user_saved_tracks()
	for item in results['items']:
		track = item['track']
		print(track['name'] + ' - ' + track['artists'][0]['name'])

def mytracks():
	playlists = spotify.user_playlists(username)
	for playlist in playlists['items']:
		if playlist['owner']['id'] == username:
			print()
			print(playlist['name'])
			print ('  total tracks', playlist['tracks']['total'])
			results = spotify.playlist(playlist['id'],
				fields="tracks,next")
			tracks = results['tracks']
			show_tracks(tracks)
			while tracks['next']:
				tracks = spotify.next(tracks)
				show_tracks(tracks)

def show_tracks(tracks):
	for i, item in enumerate(tracks['items']):
		track = item['track']
		print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
			track['name']))


def searchtrackbyartist(name):
	if name == "":
		return []
	results = spotify.search(q='artist:' + name, type='track', limit=50)
	items = results['tracks']['items']
	resultlist = generateTrackList(items)
	#pprint.pprint(resultlist)
	return resultlist

def searchtrackbyAlbum(name, artist):
	if name == "":
		return []
	results = spotify.search(q='album:' + name + " artist:" + artist, type='track', limit=50)
	items = results['tracks']['items']
	resultlist = generateTrackList(items)
	#pprint.pprint(resultlist)
	resultlist = sorted(resultlist ,  key=lambda x: x['tracknumber'])
	return resultlist


def searchtrack(name):
	if name == "":
		return []
	results = spotify.search(q= name, type='track', limit=50)
	items = results['tracks']['items']
	resultlist = generateTrackList(items)
	#pprint.pprint(resultlist)
	return resultlist


	

def formatDuration(ms):
	s=ms/1000
	m,s=divmod(s,60)
	h,m=divmod(m,60)
	d,h=divmod(h,24)
	d=d
	return str(int(m)) + ":" + str(int(s)).zfill(2)


def generateTrackList(tracks):
	resultlist = []
	count = 0
	for track in tracks:
		count = count+1
	for track in tracks:
		#pprint.pprint(track)
		artistlist, otherartists = generateArtistList(track['artists'])
		resultlist.append({
			"name":			str(track['name']), 
			"artists":		artistlist, 
			"artist":		track['artists'][0]["name"],
			"otherartists":	otherartists,
			"share":		track['external_urls']['spotify'], 
			"uri":			track['uri'],
			"duration": 	formatDuration(track['duration_ms']),
			"album": 		track['album']['name'],
			"tracknumber":	str(track['track_number']).zfill(2),
			"popularity":	str(track['popularity']),
			"preview_url":	track['preview_url'],
			"album_image":	track['album']['images'][0]['url']
		})
	return resultlist


def generateArtistList(artists):
	artistlist = str(artists[0]['name'])
	otherartists = ""
	for artist in artists[1:]:
		artistlist = artistlist + ", " + str(artist['name'])
		otherartists = otherartists + ", " + str(artist['name'])
	return artistlist, otherartists[1:].lstrip()



def download_spotify_track(song):
	#  LOGIC HERE
	#song = ""
	sys.argv.append('-s')
	sys.argv.append(song)
	sys.argv.append('--overwrite')
	sys.argv.append('force')
	sys.argv.append('--trim-silence')
	sys.argv.append('-f')
	#sys.argv.append(str(os.getcwd()) + "/queue")
	sys.argv.append(os.getcwd())

	#pool = Pool(processes=1)
	#result = pool.apply_async(func=get_track, callback=on_finish_get_track)
	#return render_template('mainpage.html', status='Download in progress', show_back_button=True)
	dlr()

def dlr():
	const.args = handle.get_arguments()

	internals.filter_path(const.args.folder)
	youtube_tools.set_api_key()

	try:
		if const.args.song:
			for track in const.args.song:
				print(track)
				track_dl = downloader.Downloader(raw_song=track)
				track_dl.download_single()
	except KeyboardInterrupt as e:
		print("Exception occured in method 'get_track':", e)
		return False
	return True

