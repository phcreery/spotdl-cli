import npyscreen
import curses
import lib.spotq as sp
from lib.TrackField import TrackList
from lib.AlbumTrackField import AlbumTrackList
from lib.ArtistTrackField import ArtistTrackList
from lib.DetailField import DetailView

class DetailForm(npyscreen.FormBaseNewExpanded): #TitlelessForm, FormBaseNew

	def create(self):

		self.add_event_hander("event_update_detail_form", self.event_update_detail_form)
		self.add_event_hander("event_new_song_byAlbum", self.event_new_song_byAlbum)
		self.add_event_hander("event_new_song_byArtist", self.event_new_song_byArtist)
		#self.add_event_hander("event_song_select", self.event_song_select)

		new_handlers = {
			curses.ascii.ctrl(curses.ascii.BS): self.exit_func,
			"b": self.ev_goback,
			"^D": self.ev_download_song,
			#"^Q": self.ev_add_queue,
		}
		self.add_handlers(new_handlers)

		column_height = terminal_dimensions()[0] - 8

		self.DetailView_widget = self.add(
			DetailView,
			name			 = "SONG",
			relx			 = 2,
			rely 			 = 1,
			max_height 		 = 6,
			#value			 = "asdf",
			editable		 = False
		)
		
		self.AlbumList_widget = self.add(
			AlbumTrackList,
			name			 = "ALBUM: ", 
			relx			 = 2,
			rely			 = 7,
			max_height 		 = int(column_height/2)
		)
		self.AlbumList_widget.setEditCallback("event_new_song_byAlbum")

		self.ArtistList_widget = self.add(
			ArtistTrackList,
			name			 = "ARTIST: ",
			relx			 = 2,
			rely			 = int(column_height/2)+7,
			max_height		 = column_height - int(column_height/2)
		)
		self.ArtistList_widget.setEditCallback("event_new_song_byArtist")
	
	def event_new_song_byAlbum(self, event):
		self.parentApp.passinfo = self.AlbumList_widget.getSelectedSongInfo()
		self.parentApp.queue_event(npyscreen.Event("event_update_detail_form"))
		#pass

	def event_new_song_byArtist(self, event):
		self.parentApp.passinfo = self.ArtistList_widget.getSelectedSongInfo()
		self.parentApp.queue_event(npyscreen.Event("event_update_detail_form"))
		#pass

	def event_update_detail_form(self, event):
		self.DetailView_widget.setvalue(self.parentApp.passinfo)

		self.AlbumList_widget.name = "ALBUM: " + self.parentApp.passinfo['album']
		self.ArtistList_widget.name = "ARTIST: " + self.parentApp.passinfo['artist']
		
		info = sp.searchtrackbyartist(self.parentApp.passinfo['artist'])
		self.ArtistList_widget.generateTrackList(info)

		info = sp.searchtrackbyAlbum(self.parentApp.passinfo['album'], self.parentApp.passinfo['artist'])
		self.AlbumList_widget.generateTrackList(info)
		count = 0
		for track in info:
			count = count+1
		self.AlbumList_widget.footer = str(count) + " Tracks"

		self.display()
		self.DetailView_widget.display()
		self.AlbumList_widget.display()
		self.ArtistList_widget.display()
		
	def ev_goback(self, event):
		self.parentApp.switchForm("MAIN")

	def event_albumsong_select(self, event):
		pass		

	def ev_download_song(self, event):
		self.ev_add_queue("event")
		self.goto_download()

	def ev_add_queue(self, event):
		self.parentApp.queue_event(npyscreen.Event("event_add_queue"))

	def goto_download(self):
		#self.parentApp.passinfo = self.TrackList_widget.getSelectedSongInfo()
		self.parentApp.queue_event(npyscreen.Event("event_start_download"))
		self.parentApp.setNextForm("DOWN")
		#self.parentApp.setNextFormPrevious()
		self.parentApp.switchForm("DOWN")	

	def exit_func(self, _input):
		exit(0)

	#def while_waiting(self):
		#current_user = self.parentApp.mainform.TrackList_widget.getSelectedSongInfo()['album']
		
		#self.AlbumList_widget.name = "ALBUM: " + self.parentApp.passinfo['album']
		#npyscreen.Event("event_update_main_form")
		#self.parent.parentApp.queue_event(npyscreen.Event("event_update_main_form"))





def terminal_dimensions():
	return curses.initscr().getmaxyx()