import spotipy
import spotipy.util as util
import pprint
import os


username = "phcreery"
scope = 'user-library-read'
token = util.prompt_for_user_token(username,scope,client_id='46508b20d6e7448dad0476c7162efffb',client_secret='2f9cefbfa0544dd38e245047217909ef',redirect_uri='http://localhost:8888/callback')

os.system("clear")

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
			"popularity":	str(track['popularity'])
		})
	return resultlist


def generateArtistList(artists):
	artistlist = str(artists[0]['name'])
	otherartists = ""
	for artist in artists[1:]:
		artistlist = artistlist + ", " + str(artist['name'])
		otherartists = otherartists + ", " + str(artist['name'])
	return artistlist, otherartists[1:].lstrip()