import npyscreen
import curses
from lib.DetailField import DetailView
from lib.FolderField import FolderField
from lib.NotifyPopup import notify

import time

import pickle
import json
import os
import glob

class CollectionForm(npyscreen.FormBaseNewExpanded):	#Form, FormBaseNew, ActionForm
	
	def create(self):
		
		self.add_event_hander("event_folder_select", self.event_folder_select)
		self.add_event_hander("event_update_CollectionForm_form", self.event_update_collection_form)
		
		new_handlers = {
			# Set ctrl+Q to exit
			#"^Q": self.exit_func,
			# Set alt+enter to clear boxes
			#curses.ascii.alt(curses.ascii.NL): self.selectsong,
			#curses.ascii.NL: self.selectsong,
			#"^R": self.inputbox_clear,
			"b": self.ev_goback,
			"r": self.event_update_collection_form,
			"u": self.ev_up_dir,
			"s": self.ev_goback,
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

		self.folders = []
		self.query_songs()

		self.Folders_widget = self.add(
			FolderField,
			name			 = "FOLDERS",
			relx			 = 2,
			rely			 = 4,
			max_height		 = column_height - 3,
			value			 = self.folders,
			editable		 = True,
			scroll_exit		 = False,
			footer			 = "[U]p [S]et"
		)
		self.Folders_widget.setEditCallback("event_folder_select")
		#self.folders = []

	def event_folder_select(self, event):
		self.parentApp.save_location = self.parentApp.save_location + self.Folders_widget.getSelectedInfo() + "/"
		self.query_songs()
		self.event_update_collection_form("event")

	def ev_up_dir(self, event):
		self.parentApp.save_location = self.parentApp.save_location.rsplit('/', 2)[0] + "/"
		with open('some_file.txt', 'w') as f:
			json.dump(self.parentApp.save_location, f)
		self.event_update_collection_form("event")


	def query_songs(self):
		#self.folders = next(os.walk(self.parentApp.save_location))[1]
		songlist = glob.glob("/mnt/c/Users/phcre/Music/*.mp3")
		#songs = ""
		#for song in songlist: 
		#	songs = songs + song.rsplit('.', 1)[0].rsplit('/', 1)[1] + "\n"
		self.songlist = songlist
		#return songs


	def event_update_collection_form(self, event):
		self.query_songs()
		self.Folders_widget.assignvalues(self.folders)
		self.Directory_widget.value = self.parentApp.save_location
		self.Directory_widget.update()
		self.Folders_widget.update()
		self.Directory_widget.display()
		self.Folders_widget.display()

	def ev_goback(self, event):
		self.parentApp.switchFormPrevious()

def terminal_dimensions():
	return curses.initscr().getmaxyx()


