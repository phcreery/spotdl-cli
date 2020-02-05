import npyscreen
import textwrap 
import curses

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

	def log(self, value):
		#h,w = terminal_dimensions()
		h = self.height - 1
		w = self.width

		valuelist = self.value.split('\n')

		value = textwrap.fill(value, w)
		self.value = self.value + str(value) + "\n"

		#valuelist.append(value)
		#self.value = str(self.value) + str(value) + "\n"

		valuelist = self.value.split('\n')
		while len(valuelist) > h:
			valuelist.pop(0)
		self.value = '\n'.join(map(str, valuelist))
