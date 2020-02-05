import npyscreen
import curses
import lib.spotq as sp
from lib.TrackField import TrackList
from lib.DetailField import DetailView
from lib.QueueField import QueueList
from lib.NotifyPopup import notify

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
			"b": self.ev_goback,
			"d": self.event_start_download
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
			scroll_exit		 = False,
			footer			 = "D to download"
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
		#self.keypress_timeout = 10
		self.isdownloading = False
		
	def event_add_queue(self, event):
		#self.Console_widget.log("event_add_queue called")
		self.queue.append(self.parentApp.passinfo)
		self.Queue_widget.assignvalues(self.queue)
		#npyscreen.notify("Queued", title='Popup Title')
		#npyscreen.notify_confirm("Queued", title='Popup Title', form_color='STANDOUT', editw = 5)
		notify("Queued", title='Notice')
		time.sleep(0.5) # needed to have it show up for a visible amount of time
		npyscreen.blank_terminal()	# needed to cleat notify form residue
		#self.event_update_download_form("event")

	def event_start_download(self, event):
		self.Console_widget.log("event_start_download called")
		if len(self.queue) > 0:
			self.isdownloading = True
		else:
			notify("Queue is Empty", title='Warning')
			time.sleep(2)
			npyscreen.blank_terminal()
			self.isdownloading = False
			return

		self.current_song = self.queue[0]
		self.Console_widget.log("Downloading: " + self.current_song['name'] + " by " + self.current_song['artists'])
		#self.Console_widget.name = self.parentApp.passinfo['name']
		self.Console_widget.footer = self.current_song['name'] + " | Running"
		
		self.executecommand = "python3 spotdlRunner.py --song " + self.current_song['share'] + " --overwrite force --trim-silence"
		#self.executecommand = "spotdl --song "
		#self.executecommand = "sudo ls -la npyscreen >&2 "
		
		self.Console_widget.log(">_ " + self.executecommand)
		self.event_update_download_form("event")
		self.process = self.run_command(self.executecommand)


	def download_handler(self):
		if self.isdownloading == True and hasattr(self, 'process'):
			pass
		else:
			self.queue.pop(0)
			#self.que_next()
			self.event_start_download("event")
			

	def event_update_download_form(self, event):
		#self.Console_widget.log("Updating Form...")
		self.Queue_widget.assignvalues(self.queue)
		self.Queue_widget.update()
		self.Console_widget.update()
		#self.Queue_widget.display()
		self.Console_widget.display()
		#self.Console_widget.log("Done Updating")
		#self.display()			# Don't use this, it causes que list to blank until interacted

	def ev_goback(self, event):
		self.parentApp.switchFormPrevious()

	def run_command(self, command):
		self.Console_widget.log("Starting Process...")
		process = subprocess.Popen(shlex.split(command), stderr=subprocess.PIPE, encoding='utf8')
		# add stdout=subprocess.PIPE, for other commands
		return process

	def command_output(self, process):
		output = process.stderr.readline() # process.stdout.readline()
		#output = process.communicate()
		if output == '' and process.poll() is not None:
			return None
		if output:
			return output.strip()
		#rc = process.poll()
		#return rc

	def command_done(self):
		self.Console_widget.footer = "Stopped"
		delattr(self, 'process')
		self.Console_widget.log("Done")
		pass

	def while_waiting(self):
		#self.Console_widget.log("WhileWait Loop")
		if self.isdownloading == True: 
			self.download_handler()
		if hasattr(self, 'process'):
			results = self.command_output(self.process)
			if results != None:
				self.Console_widget.log(results)
			else:
				self.command_done()

		self.event_update_download_form("event")
		#self.Queue_widget.update()
		#self.Console_widget.update()


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


