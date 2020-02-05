#import npyscreen
import textwrap

from npyscreen import fmPopup
from npyscreen import wgmultiline
from npyscreen import fmPopup
import curses

from npyscreen import fmForm
from npyscreen import fmActionFormV2

class MyPopup(fmForm.Form):
	DEFAULT_LINES	 = 2
	DEFAULT_COLUMNS	 = 20
	SHOW_ATX		 = 40
	SHOW_ATY		 = 4


def notifyr(message, title="Message", form_color='STANDOUT', 
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