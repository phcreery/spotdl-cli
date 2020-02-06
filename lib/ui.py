import npyscreen
from lib.SearchForm import SearchForm
from lib.DetailForm import DetailForm
from lib.DownloadForm import DownloadForm
from lib.DirectoryForm import DirectoryForm
import curses
from lib.theme import MyTheme



class App(npyscreen.StandardApp):	#StandardApp, NPSAppManaged, NPSApp

	passinfo = {}
	#curses.use_default_colors()
	save_location = "/mnt/c/Users/phcre/Documents/Python/spoticli/"

	def onStart(self):
		npyscreen.setTheme(MyTheme) 
		#TransparentThemeLightText, TransparentThemeDarkText, TrueTransparentThemeDarkText
		#self.mainform = self.addForm('MAIN', initForm, name='Spotify')
		self.mainform = self.addForm('MAIN', SearchForm)
		self.detailform = self.addForm('SECOND', DetailForm)
		self.dlform = self.addForm('DOWN', DownloadForm)
		self.saveform = self.addForm('DIR', DirectoryForm)

		
	def change_form(self, name):
		# Switch forms.  NB. Do *not* call the .edit() method directly (which 
		# would lead to a memory leak and ultimately a recursion error).
		# Instead, use the method .switchForm to change forms.
		self.switchForm(name)


