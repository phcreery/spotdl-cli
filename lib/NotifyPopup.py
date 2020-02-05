#import npyscreen
import textwrap

#from npyscreen import fmPopup
from npyscreen import wgmultiline
import curses

from npyscreen import fmForm
#from npyscreen import fmActionFormV2

class MyPopup(fmForm.Form):
	h,w = curses.initscr().getmaxyx()
	DEFAULT_LINES	 = 5
	DEFAULT_COLUMNS	 = 20
	SHOW_ATX		 = int( w/2 - DEFAULT_COLUMNS/2 )
	SHOW_ATY		 = int( h/2 - DEFAULT_LINES/2 ) - 2


def notify(message, title="Message", form_color='STANDOUT', 
			wrap=True, wide=False,
			):
	message = _prepare_message(message)
	F = MyPopup(name=title, color=form_color)
	F.preserve_selected_widget = True
	mlw = F.add(wgmultiline.Pager,)
	mlw_width = mlw.width-1
	if wrap:
		message = _wrap_message_lines(message, mlw_width)
	mlw.values = message
	F.display()

def notify_wait(*args, **keywords):
	notify(*args, **keywords)
	curses.napms(3000)
	curses.flushinp()



def _prepare_message(message):
	if isinstance(message, list) or isinstance(message, tuple):
		return "\n".join([ s.rstrip() for s in message])
		#return "\n".join(message)
	else:
		return message

def _wrap_message_lines(message, line_length):
	lines = []
	for line in message.split('\n'):
		lines.extend(textwrap.wrap(line.rstrip(), line_length))
	return lines


