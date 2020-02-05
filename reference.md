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

## npyscreen/

### wgwidget.py:

add
```
368        mx = mx+1
369        my = my+1
```
removes padding on right & bottom

### fmFooter.py:
Line: 446 add:
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
This creates a new from type without a border and title


### \__init\__.py
Line: 14 modify
```
from   .fmForm                  import FormBaseNew, Form, TitleForm, TitleFooterForm, SplitForm, FormExpanded, FormBaseNewExpanded, blank_terminal, TitlelessForm
```
Incluse my new form type

### wgtextbox.py:

Line: 250 from
```
if not string_to_print or place_in_string > len(string_to_print)-1:
```
to   
```
if not string_to_print or place_in_string > len(string_to_print)-0:
```

Line: 47 from
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

Both of these allow for the list & text fields to be full width, leaving only 1 space to the right and 1 to the left




## spotdl/

### youtube_tools.py

Line: 183 (in download_song()) modify
```
link.download(filepath=filepath, quiet=True, callback=mycb)
```

After download function, add
```
def mycb(total, recvd, ratio, rate, eta):
    #log.info("Dl: " + str(recvd), str(int(ratio)*100)+"%", "ETA: "+eta)
	log.info(str(round(float(ratio)*100,2))+"%" + "  " + "Bytes: " + str(recvd))
	#print("Dl: " + str(recvd), str(int(ratio)*100)+"%", "ETA: "+str(eta))

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

