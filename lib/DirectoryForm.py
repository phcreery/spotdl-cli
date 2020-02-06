import npyscreen
import curses
#import lib.spotq as sp
#from lib.TrackField import TrackList
from lib.DetailField import DetailView
from lib.QueueField import QueueList
from lib.NotifyPopup import notify

import time
import subprocess
import shlex

import pickle
import json
import os
import signal

class DirectoryForm(npyscreen.FormBaseNewExpanded):	#Form, FormBaseNew, ActionForm
	
	def create(self):
		
		self.add_event_hander("event_folder_select", self.event_folder_select)
		#self.add_event_hander("event_start_download", self.event_start_download)
		
		new_handlers = {
			# Set ctrl+Q to exit
			#"^Q": self.exit_func,
			# Set alt+enter to clear boxes
			#curses.ascii.alt(curses.ascii.NL): self.selectsong,
			#curses.ascii.NL: self.selectsong,
			#"^R": self.inputbox_clear,
			"b": self.ev_goback,
			"u": self.,
			"s": self.,
		}
		self.add_handlers(new_handlers)
		

		column_height = terminal_dimensions()[0] - 2

		self.Directory_widget = self.add(
			DetailView,
			#name			 = "DIRECTORY",
			relx			 = 2,
			rely			 = 1,
			max_height		 = 3,
			value			 = self.parentApp.save_location,
			editable		 = False,
			#footer			 = "Ctrl+D to download"
		)

		self.Folders_widget = self.add(
			QueueList,
			name			 = "FOLDERS",
			relx			 = 2,
			rely			 = 4,
			max_height		 = column_height - 5,
			#value			 = "asdf",
			editable		 = True,
			scroll_exit		 = False,
			footer			 = "[U]p [S]elect"
		)
        self.Folders_widget.setEditCallback("event_folder_select")
        self.folders = []

    def event_folder_select(self, event):
        pass

    def event_update_download_form(self, event):
        self.Queue_widget.assignvalues(self.folders)
		self.Directory_widget.update()
		self.Folders_widget.update()

	def ev_goback(self, event):
		self.parentApp.switchFormPrevious()

def terminal_dimensions():
	return curses.initscr().getmaxyx()


