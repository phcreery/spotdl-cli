import npyscreen
import curses

# Set your theme class name as MyTheme and rename the other

class MyTheme2(npyscreen.ThemeManager):
	default_colors = {
	'DEFAULT'    : 'WHITE_BLACK',
	'FORMDEFAULT' : 'WHITE_BLACK',
	'NO_EDIT'    : 'BLUE_BLACK',
	'STANDOUT'  : 'CYAN_BLACK',
	'CURSOR'      : 'WHITE_BLACK',
	'CURSOR_INVERSE': 'BLACK_WHITE',
	'LABEL'    : 'GREEN_BLACK',
	'LABELBOLD'   : 'WHITE_BLACK',
	'CONTROL'    : 'YELLOW_BLACK',
	'IMPORTANT'   : 'GREEN_BLACK',
	'SAFE'    : 'GREEN_BLACK',
	'WARNING'    : 'YELLOW_BLACK',
	'DANGER'      : 'RED_BLACK',
	'CRITICAL'  : 'BLACK_RED',
	'GOOD'    : 'GREEN_BLACK',
	'GOODHL'      : 'GREEN_BLACK',
	'VERYGOOD'  : 'BLACK_GREEN',
	'CAUTION'    : 'YELLOW_BLACK',
	'CAUTIONHL'   : 'BLACK_YELLOW',
	}


class MyTheme(npyscreen.ThemeManager):
	_colors_to_define = ( 

	('BLACK_ON_DEFAULT',   curses.COLOR_BLACK,    -1),
	('WHITE_ON_DEFAULT',   curses.COLOR_WHITE,    -1),
	('BLUE_ON_DEFAULT', curses.COLOR_BLUE,      -1),
	('CYAN_ON_DEFAULT', curses.COLOR_CYAN,      -1),
	('GREEN_ON_DEFAULT',   curses.COLOR_GREEN,    -1),
	('MAGENTA_ON_DEFAULT', curses.COLOR_MAGENTA,    -1),
	('RED_ON_DEFAULT',   curses.COLOR_RED,        -1),
	('YELLOW_ON_DEFAULT',  curses.COLOR_YELLOW,  -1),
	)

	_color_values = (
		# redefining a standard color
		#(curses.COLOR_GREEN, (150,250,100)),
		(curses.COLOR_BLACK, (400,400,400)),
		# defining another color
		#(70, (150,250,100)),
	)

	default_colors = {
		'DEFAULT'    : 'WHITE_ON_DEFAULT', # Text Color
		'FORMDEFAULT' : 'WHITE_ON_DEFAULT', # Border Color for completed form
		'NO_EDIT'    : 'BLACK_ON_DEFAULT',
		'STANDOUT'  : 'RED_ON_DEFAULT', # Popup
		'CURSOR'      : 'BLACK_ON_DEFAULT',
		'CURSOR_INVERSE': 'BLACK_ON_DEFAULT',
		'LABEL'    : 'BLACK_ON_DEFAULT', # Header and Footer
		'LABELBOLD'   : 'WHITE_ON_DEFAULT',
		'CONTROL'    : 'RED_ON_DEFAULT',
		'WARNING'    : 'RED_ON_DEFAULT',
		'CRITICAL'  : 'RED_ON_DEFAULT',
		'GOOD'    : 'GREEN_ON_DEFAULT',
		'GOODHL'      : 'GREEN_ON_DEFAULT',
		'VERYGOOD'  : 'BLACK_ON_DEFAULT',
		'CAUTION'    : 'YELLOW_ON_DEFAULT',
		'CAUTIONHL'   : 'BLACK_ON_DEFAULT',
	}


	def __init__(self, *args, **keywords):
		curses.use_default_colors()  # For transparency
		super(MyTheme, self).__init__(*args, **keywords)
