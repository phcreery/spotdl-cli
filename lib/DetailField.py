import npyscreen

class DetailView(npyscreen.BoxTitle):
	_contained_widget = npyscreen.MultiLineEdit

	def setvalue(self, value):
		dispinfo = ""
		dispinfo = dispinfo + "Song:    " + value['name'] + "\n"
		dispinfo = dispinfo + "Album:   " + value['album'] + "\n"
		dispinfo = dispinfo + "Artist:  " + value['artists'] + "\n"
		dispinfo = dispinfo + "Length:  " + str(value['duration'])
		#dispinfo = str(value)
		self.value = dispinfo