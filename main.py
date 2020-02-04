from lib.ui import App
import lib.spotq as sp
import pprint

import subprocess
import shlex

from spotdl.spotdl import dlr

#npyscreen.disableColor()

def main():
	#results = sp.searchtrack("Roses SoMo")
	#results = sp.searchtrackbyartist("SoMo")
	#results = sp.searchtrackbyAlbum("Ride", "SoMo")
	#print(results)
	#pprint.pprint(results)
	#mytracks()

	"""
	cmd = run_command("spotdl --song 'this feeling'")
	while True:	
		output, rc = command_output(cmd)
		if output == None:
			break
		else:
			print(output, rc)
	"""

	dlr('this feeling')

	#app = App()
	#app.run()


def run_command(command):
	process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, encoding='utf8')
	return process

def command_output(process):
	output = process.stdout.readline()
	if output == '' and process.poll() is not None:
		return None
	if output:
		val =  output.strip()
		#print(output.strip())
	rc = process.poll()
	return val, rc


if __name__ == "__main__":
	main()

