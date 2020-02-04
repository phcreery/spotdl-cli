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
		h,w = terminal_dimensions()

		valuelist = self.value.split('\n')

		value = textwrap.wrap(value, w - 4)
		valuelist.append(value)
		#self.value = str(self.value) + str(value) + "\n"
		
		while len(valuelist) > h - 4:
			valuelist.pop(0)
		
		self.value = '\n'.join([str(elem) for elem in valuelist]).strip('[]')

def terminal_dimensions():
	return curses.initscr().getmaxyx()