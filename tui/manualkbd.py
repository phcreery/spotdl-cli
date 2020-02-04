import os
#from .kbd import keyarray, drawtxtbox
#import .kbd as kbd
#import .kbd
import tui.kbd as kbd


class manualkbdinput():
    def __init__(self):
        self.a=0
        self.x=0
        self.y=0
        self.z=0 
        self.kbd=True
        self.keystr=""
        #return(x,y,z,a,kbd)

    def sendkbdinput(self,command):
        #x,y,z,a,kbd = status
        #char = getch()
        #kbd=True
        self.a=0
        if (command == "exit"):
            #print("Stop!")
            self.kbd=False
            #exit(0)

        elif (command == "left"):
            self.x=self.x-1
        elif (command == "right"):
            self.x=self.x+1
        elif (command == "up"):
            self.y=self.y-1
        elif (command == "down"):
            self.y=self.y+1
        elif (command == "+"):
            self.z=self.z+1
        elif (command == "-"):
            self.z=self.z-1
        elif (command == "select"):
            #self.a=1
            self.keystr = self.keystr + kbd.keyarray[self.z][self.y][self.x]
        elif (command == "backspace"):
            self.a=-1

        #return(x,y,z,a,kbd)

    def sendkbdtext(self,text):
        self.keystr = self.keystr + text

    def drawkbdinput(self,title,dispsize,size,tooltip):
        #x,y,z,a,kbd = status
        height, width = dispsize

        os.system("clear")
        #x = random.randint(0, len(keyarray[0][0])-1)f
        #y = random.randint(0, len(keyarray[0])-1)
        #z = random.randint(0, len(keyarray)-1)

        #if self.a == 1:
        #    self.keystr = self.keystr + keyarray[self.z][self.y][self.x]

        #rows, columns = os.popen('stty size', 'r').read().split()
        #print("start")
        print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")
        kbd.drawtxtbox(title, self.keystr, width)
        print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")
        #print()
        if size == "big":
            kbd.drawkbdbig(self.x,self.y, kbd.keyarray[self.z], width)
        elif size == "medium":
            kbd.drawkbdmedium(self.x,self.y, kbd.keyarray[self.z], width)
        elif size == "small":
            kbd.drawkbdsmall(self.x,self.y, kbd.keyarray[self.z], width)
        elif size == "giant":
            kbd.drawkbdgiant(self.x,self.y, kbd.keyarray[self.z], width)

        print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")
        print("".join(" " for x in range(0, int(round((width-len(tooltip))/2)) )), end="")
        print(tooltip)
        #x,y,z,a,kbd = getinput(x,y,z,kbd)

        self.x = kbd.clamp(self.x, 0, len(kbd.keyarray[0][0])-1)
        self.y = kbd.clamp(self.y, 0, len(kbd.keyarray[0])-1)
        self.z = kbd.clamp(self.z, 0, len(kbd.keyarray)-1)

        

        return(self.keystr)
