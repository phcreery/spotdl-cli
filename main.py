from lib.ui import App
import lib.spotq as sp
import pprint
from lib.spotq import download_spotify_track


import subprocess
import shlex
import os
import requests
import vlc
import glob
import time
import json

#from spotdl.spotdl import dlr

#npyscreen.disableColor()

def main():
	#test_spotq()
	#test_cmd()
	#export_songlist()

	app = App()
	app.run()


def test_spotq():
	#results = sp.searchtrack("Roses SoMo")
	#results = sp.searchtrackbyartist("SoMo")
	#results = sp.searchtrackbyAlbum("Ride", "SoMo")
	#print(results)
	#pprint.pprint(results)
	#mytracks()

	#print(os.getcwd())
	#download_spotify_track('this feeling')

	DownloadFile("https://p.scdn.co/mp3-preview/3eb16018c2a700240e9dfb8817b6f2d041f15eb1?cid=774b29d4f13844c495f206cafdad9c86")
	p = vlc.MediaPlayer("file:///mnt/c/Users/phcre/Documents/Python/spoticli/track.mp3")
	p.play()


def test_cmd():
	cmd = run_command("python3 spotdlRunner.py --song 'https://open.spotify.com/track/3PP9CXeE0PYaM5GIGQqBIV' --overwrite force --trim-silence")
	while True:	
		output, rc = command_output(cmd)
		if output == None:
			break
		else:
			print(output, rc)



def export_songlist():
	songlist = glob.glob("/mnt/c/Users/phcre/Music/old/*.mp3")
	songs = ""
	for song in songlist:
		songs = songs + song.rsplit('.', 1)[0].rsplit('/', 1)[1] + "\n"
	print(songs)
	with open('some_file.txt', 'w') as f:
		f.write(songs)
		#json.dump(songs, f)
	time.sleep(1)



def DownloadFile(url):
	local_filename = url.split('/')[-1]
	r = requests.get(url)
	f = open(local_filename, 'wb')
	for chunk in r.iter_content(chunk_size=512 * 1024): 
		if chunk: # filter out keep-alive new chunks
			f.write(chunk)
	f.close()
	return 

def run_command(command):
	#process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, encoding='utf8')
	process = subprocess.Popen(shlex.split(command), stderr=subprocess.PIPE, encoding='utf8')
	return process

def command_output(process):
	output = process.stderr.readline() # process.stdout.readline()
	if output == '' and process.poll() is not None:
		return None
	if output:
		val =  output.strip()
		#print(output.strip())
	rc = process.poll()
	return val, rc


if __name__ == "__main__":
	main()
	exit()

