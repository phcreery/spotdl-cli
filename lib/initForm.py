import npyscreen
import curses
import lib.spotq as sp
from lib.TrackField import TrackList
from lib.DetailField import DetailView
from .theme import MyTheme

class initForm(npyscreen.ActionForm):	#Form, FormBaseNew, ActionForm
	
	def create(self):
		curses.use_default_colors()
		npyscreen.setTheme(MyTheme) 
		#self.parentApp.switchForm("PRI")

	def beforeEditing(self):
		self.parentApp.switchForm("PRI")

	def on_ok(self):
		# Exit the application if the OK button is pressed.
		self.parentApp.switchForm("PRI")