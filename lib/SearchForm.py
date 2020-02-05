import npyscreen
import curses
import lib.spotq as sp
from lib.TrackField import TrackList
from lib.DetailField import DetailView
import time

class SearchForm(npyscreen.TitlelessForm):	#Form, FormBaseNew, ActionForm, TitleForm, TitleFooterForm, FormBaseNewExpanded, FormExpanded, 
	
	def create(self):
		
		self.add_event_hander("event_value_edited", self.event_value_edited)
		self.add_event_hander("event_song_select", self.event_song_select)
		
		new_handlers = {
			# Set ctrl+Q to exit
			#"^Q": self.ev_add_queue,
			# Set alt+enter to clear boxes
			curses.ascii.alt(curses.ascii.NL): self.exit_func,
			#curses.ascii.NL: self.ev_selectsong,
			"^R": self.ev_inputbox_clear,
			"d": self.ev_download_song,
			"^O": self.ev_selectsong,
			"b": self.exit_func
		}
		self.add_handlers(new_handlers)

		column_height = terminal_dimensions()[0] - 11
		width = terminal_dimensions()[1] - 2

		self.SearchBox_widget = self.add(
			SearchBox,
			name			 = "SEARCH",
			max_height 		 = 3,
			#max_width 		 = width,
			relx			 = 1,
			#rely			 = 0,
			value			 = "",
			#labelColor		 ='LABEL',
			safe_2_exit 	 = False
		)
		
		self.TrackList_widget = self.add(
			TrackList, 
			name			 = "SONGS",
			#relx			 = 2,
			rely			 = 4,
			max_height		 = column_height,
			scroll_exit		 = True,
			#value_changed_callback = self.event_song_select
		)
		self.TrackList_widget.setEditCallback("event_song_select")
		

		self.DetailView_widget = self.add(
			DetailView,
			#name			 = "INFO",
			#relx			 = 2,
			rely			 = column_height+4,
			max_height		 = 6,
			#value			 = "asdf",
			editable		 = False,
			footer			 = "Ctrl+D to download, Shift+Enter to open"
		)
		#self.edit()

		#self.event_value_edited("event")
	

	def event_value_edited(self, event):
		if "\n" in self.SearchBox_widget.value:
			self.SearchBox_widget.value = self.SearchBox_widget.value.replace('\n', '').replace('\r', '')
			#self.TrackList_widget.value = 0
			self.TrackList_widget.values = []
			self.update_results()
			
		#self.TrackList_widget.when_value_edited()

	def update_results(self):
		info = sp.searchtrack(self.SearchBox_widget.value)
		self.TrackList_widget.generateTrackList(info)
		self.TrackList_widget.update(clear=True)
		#self.DetailView_widget.update()
		self.display()
		#self.TrackList_widget.update(clear=True)
		
	def event_song_select(self, event):
		if self.TrackList_widget.value != None:
			self.DetailView_widget.setvalue(self.TrackList_widget.getSelectedSongInfo())
			self.DetailView_widget.update()

	def ev_inputbox_clear(self, _input):
		self.SearchBox_widget.value = self.DetailView_widget.value = self.TrackList_widget.values = ""
		#self.SearchBox_widget.display()
		#self.TrackList_widget.display()
		#self.DetailView_widget.display()
		self.display()
	
	def ev_download_song(self, event):
		self.ev_add_queue("event")
		self.goto_download()

	def ev_add_queue(self, event):
		#npyscreen.notify("Added", title='Popup Title')
		#time.sleep(1)
		self.parentApp.passinfo = self.TrackList_widget.getSelectedSongInfo()
		self.parentApp.queue_event(npyscreen.Event("event_add_queue"))

	def goto_download(self):
		self.parentApp.passinfo = self.TrackList_widget.getSelectedSongInfo()
		self.parentApp.queue_event(npyscreen.Event("event_start_download"))
		self.parentApp.setNextForm("DOWN")
		#self.parentApp.setNextFormPrevious()
		self.parentApp.switchForm("DOWN")	

	def ev_selectsong(self, event):
		self.parentApp.passinfo = self.TrackList_widget.getSelectedSongInfo()
		self.parentApp.queue_event(npyscreen.Event("event_update_detail_form"))
		self.parentApp.switchForm("SECOND")

	"""
	def while_waiting(self):
		results = sp.searchtrack(self.SearchBox_widget.value)
		self.TrackList_widget.values = results
		#self.DetailView_widget.value = self.TrackList_widget.value
		#self.SearchBox_widget.update_results()
		self.TrackList_widget.display ()
		self.DetailView_widget.display ()
		#npyscreen.Event("event_update_main_form")
	"""

	#def afterEditing(self):
	#	self.parentApp.setNextForm("MAIN")

	def on_ok(self):
		# Exit the application if the OK button is pressed.
		#self.ev_selectsong("go")
		self.goto_download()

	def on_cancel(self, _input):
		exit(0)

	def exit_func(self, _input):
		exit(0)



class SearchBox(npyscreen.BoxTitle):
	_contained_widget = npyscreen.MultiLineEdit #TitleText #Textfield #MultiLineEdit
	def when_value_edited(self):
		#self.display()
		#self.parent.event_value_edited("change")
		self.parent.parentApp.queue_event(npyscreen.Event("event_value_edited"))
		#self.parent.parentApp.queue_event(npyscreen.Event("event_update_main_form"))
	
	def safe_to_exit(self):
		return False


def terminal_dimensions():
	return curses.initscr().getmaxyx()