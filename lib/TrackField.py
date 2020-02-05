import npyscreen
import curses


class TrackList(npyscreen.BoxTitle): #SelectOne, BoxTitle
	#_contained_widget = npyscreen.BoxTitle
	#_contained_widget = npyscreen.MultiLine
	def when_value_edited(self):
	#def when_check_value_changed(self):
		# event to change message dialog box
		self.parent.parentApp.queue_event(npyscreen.Event(self.callback))

	def setEditCallback(self, value):
		self.callback = value

	def generateTrackList(self, values):
		w = self.width
		space = int((w-10)/2)
		#space2 = int((w-12)/2)
		newvalues = []
		for song in values:
			newvalue = self.tabafter(song['name'], space+5) + self.tabafter(song['artists'], space-5) + song['duration']
			newvalues.append(newvalue)
		self.values = newvalues
		self.info = values

	def setinfo(self, data):
		self.info = data
	def getinfo(self):
		return self.info

	def getSelectedSongInfo(self):
		return self.info[self.value]


	def tabafter(self, data, w):
		data = (data[:w-3] + '..') if len(data) > w-3 else data
		space = " "
		for i in range(w - len(data)):
			space = space + " "
		return str(data) + space

