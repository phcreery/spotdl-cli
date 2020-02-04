# References

### Subprocess:
https://www.endpoint.com/blog/2015/01/28/getting-realtime-output-using-python
https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running


### npyscreen:
https://stackoverflow.com/questions/52414352/how-should-widgets-be-resized-in-npyscreen-a-python-curses-wrapper
https://github.com/npcole/npyscreen/
https://npyscreen.readthedocs.io/widgets-title.html#widgets-box-widgets

# Requires:
spotipy
spotdl


# MODs

## npyscreen:

> wgwidget.py:

add
```
368        mx = mx+1
369        my = my+1
```


> fmFooter.py:
446 add:
```
class TitlelessForm(FormBaseNewExpanded):
    """A form without a box, just a title line"""
    BLANK_LINES_BASE    = 1
    DEFAULT_X_OFFSET    = 1
    DEFAULT_NEXTRELY    = 1
    BLANK_COLUMNS_RIGHT = 0
    OK_BUTTON_BR_OFFSET = (1,6)
    #OKBUTTON_TYPE = button.MiniButton
    #DEFAULT_X_OFFSET = 1
    def draw_form(self):
        MAXY, MAXX = self.curses_pad.getmaxyx()
        #self.curses_pad.hline(0, 0, curses.ACS_HLINE, MAXX) 
        #self.draw_title_and_help()
```


> __init__.py
14 modify
```
from   .fmForm                  import FormBaseNew, Form, TitleForm, TitleFooterForm, SplitForm, FormExpanded, FormBaseNewExpanded, blank_terminal, TitlelessForm
```

> wgtextbox:

250
```
from if not string_to_print or place_in_string > len(string_to_print)-1:
to   if not string_to_print or place_in_string > len(string_to_print)-0:
```
47
from
```
        if self.on_last_line:
            self.maximum_string_length = self.width - 2  # Leave room for the cursor
        else:   
            self.maximum_string_length = self.width - 1  # Leave room for the cursor at the end of the string.
```
to
```
        if self.on_last_line:
            self.maximum_string_length = self.width - 1  # Leave room for the cursor
        else:   
            self.maximum_string_length = self.width - 0  # Leave room for the cursor at the end of the string.
```






# requirements.txt:

spotipy
lyricwikia
mutagen
pafy
slugify
titlecase
appdirs
bs4
logzero
spotdl

