import npyscreen
import curses
import lib.spotq as sp
from lib.TrackField import TrackList
from lib.DetailField import DetailView
from lib.QueueField import QueueList

import time
import subprocess
import shlex

class DownloadForm(npyscreen.FormBaseNewExpanded):	#Form, FormBaseNew, ActionForm
	
	def create(self):
		
		self.add_event_hander("event_add_queue", self.event_add_queue)
		self.add_event_hander("event_start_download", self.event_start_download)
		
		new_handlers = {
			# Set ctrl+Q to exit
			#"^Q": self.exit_func,
			# Set alt+enter to clear boxes
			#curses.ascii.alt(curses.ascii.NL): self.selectsong,
			#curses.ascii.NL: self.selectsong,
			#"^R": self.inputbox_clear,
			"b": self.ev_goback
		}
		self.add_handlers(new_handlers)
		self.queue = []

		column_height = terminal_dimensions()[0] - 2

		self.Queue_widget = self.add(
			QueueList,
			name			 = "QUEUE",
			relx			 = 2,
			rely			 = 1,
			max_height		 = int(column_height/2),
			#value			 = "asdf",
			editable		 = True,
			#footer			 = "Ctrl+D to download"
		)

		self.Console_widget = self.add(
			DetailView,
			name			 = "CONSOLE",
			relx			 = 2,
			rely			 = column_height - int(column_height/2),
			max_height		 = column_height - int(column_height/2),
			#value			 = "asdf",
			editable		 = False,
			#footer			 = "Ctrl+D to download"
		)
		
	def event_add_queue(self, event):
		#if self.queue == None:
		#	self.queue = []
		self.queue.append(self.parentApp.passinfo)
		self.Queue_widget.assignvalues(self.queue)
		#self.event_update_download_form("event")

	def event_start_download(self, event):
		#self.Console_widget.name = self.parentApp.passinfo['name']
		self.Console_widget.footer = self.parentApp.passinfo['name'] + " | Running"
		
		#self.executecommand = "python3 spotdlRunner.py --song 'https://open.spotify.com/track/3PP9CXeE0PYaM5GIGQqBIV' "
		self.executecommand = "python3 spotdlRunner.py --song " + self.parentApp.passinfo['share'] + " --overwrite force --trim-silence"
		#self.executecommand = "spotdl --song https://open.spotify.com/track/3PP9CXeE0PYaM5GIGQqBIV"
		#self.executecommand = "sudo ls -la npyscreen >&2 "
		
		self.process = self.run_command(self.executecommand)
		self.Console_widget.log(self.executecommand)
		self.event_update_download_form("event")

	def event_update_download_form(self, event):
		self.Queue_widget.update()
		self.Console_widget.update()
		self.Queue_widget.display()
		self.Console_widget.display()
		self.display()

	def ev_goback(self, event):
		self.parentApp.switchFormPrevious()

	def run_command(self, command):
		process = subprocess.Popen(shlex.split(command), stderr=subprocess.PIPE, encoding='utf8')
		# add stdout=subprocess.PIPE, for other commands
		#process = str(a) + str(b)
		#self.executedcommand = command
		return process

	def command_output(self, process):
		output = process.stderr.readline() # process.stdout.readline()
		#output = process.communicate()
		#output = process.stdout
		if output == '' and process.poll() is not None:
			return None
		if output:
			return output.strip()
		#rc = process.poll()
		#return rc

	def command_done(self):
		self.Console_widget.footer = "Stopped"
		pass

	def while_waiting(self):
		if hasattr(self, 'process'):
			results = self.command_output(self.process)
			if results != None:
				self.Console_widget.log(results)
			else:
				self.command_done()
		#else:
		#	self.event_start_download("a")


		#self.event_update_download_form("event")
		self.Queue_widget.update()
		self.Console_widget.update()


	def on_ok(self):
		self.parentApp.switchFormPrevious()

	def on_cancel(self):
		self.parentApp.switchFormPrevious()

	"""
	def run_command(command):
		process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, encoding='utf8')
		while True:
			output = process.stdout.readline()
			if output == '' and process.poll() is not None:
				break
			if output:
				print(output.strip())
		rc = process.poll()
		return rc
	"""




def terminal_dimensions():
	return curses.initscr().getmaxyx()
