import npyscreen
from lib.initForm import initForm
from lib.SearchForm import SearchForm
from lib.DetailForm import DetailForm
from lib.DownloadForm import DownloadForm
import curses
from lib.theme import MyTheme



class App(npyscreen.StandardApp):	#StandardApp, NPSAppManaged, NPSApp

	passinfo = {}
	#curses.use_default_colors()

	def onStart(self):
		npyscreen.setTheme(MyTheme) 
		#TransparentThemeLightText, TransparentThemeDarkText, TrueTransparentThemeDarkText
		#self.mainform = self.addForm('MAIN', initForm, name='Spotify')
		self.mainform = self.addForm('MAIN', SearchForm)
		self.detailform = self.addForm('SECOND', DetailForm)
		self.dlform = self.addForm('DOWN', DownloadForm)

		
	def change_form(self, name):
		# Switch forms.  NB. Do *not* call the .edit() method directly (which 
		# would lead to a memory leak and ultimately a recursion error).
		# Instead, use the method .switchForm to change forms.
		self.switchForm(name)

