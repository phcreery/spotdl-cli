import os
#import time
#import random
import sys, termios, tty
from .style import styleSet

#width = 40
#title="User:"
x=0

CRED = '\033[44m'
CEND = '\033[0m'

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def drawtxtbox(title,data,width,styleType):
    style = styleSet(styleType)
    #data=data[-(width-4):]
    print(style.tl, end=" ")
    print(title, end=" ")
    print("".join(style.t for x in range(0,width-2-len(title) )), end="")
    print(style.tr)
    #print("-----------------------------")
    for dat in data.split('\n'):
        print(style.l, dat, end="")
        #print(u'\u2588', end="")
        print("".join(" " for x in range(0,(width-1)-len(dat))), end="")
        print(style.r)
    print(style.bl, end="")
    print("".join(style.b for x in range(0,width)), end="")
    print(style.br)


def drawoptions(options,x,width):
    y=0
    for option in options:
        print("".join(" " for x in range( 0, int(width/(len(options)+1)) -len(option) )), end="")
        if y == x:
            print("[", end="")
            print(option, end="")
            print("]", end="")
        else:
            print(" ", end="")
            print(option, end="")
            print(" ", end="")
        y=y+1


def updateinput(x,press):
    a=0
    wait=True
    if press =="up":
        y=y-1
    elif press == "down":
        y=y+1
    elif press == "left":
        x=x-1
    elif press == "right":
        x=x+1
    elif press == "next":
        z=z+1
    elif press == "previous":
        z=z-1
    elif press == "select":
        a=1
    elif press == "back":
        a=-1
    elif press == "exit":
        wait = False
    return(x,a,wait)


def getdefaultinput():
    char = getch()
    if (char == "q"):
        press = "exit"
    elif (char == "a"):
        press = "left"
    elif (char == "d"):
        press = "right"    
    elif (char == "s"):
        press = "down"
    elif (char == "w"):
        press = "up"
    elif (char == "r"):
        press = "next"
    elif (char == "f"):
        press = "previous"
    elif (char == "c"):
        press = "back"
    elif (char == "e"):
        press = "select"
    return(press)

def prompt(title,context,options,dispsize,tooltip,getuserinput="default",styleType="default"):

    global x,a
    height, width = dispsize
    wait=True
    usedspace = 4 + len(context.split('\n'))
    if getuserinput == "default":
        getinput = getdefaultinput
    else:
        getinput = getuserinput
    while wait == True:
        os.system("clear")
        #print("start")
        print("".join("\n" for x in range(0, int(round((height-usedspace)/3)) )), end="")
        drawtxtbox(title, context, width-4,styleType)
        print("".join("\n" for x in range(0, int(round((height-usedspace)/3)) )), end="")
        #print()
        drawoptions(options,x,width)
        print("".join("\n" for x in range(0, int(round((height-usedspace)/3)) )), end="")
        print("".join(" " for x in range(0, int(round((width-len(tooltip))/2)) )), end="")
        print(tooltip)

        x,a,wait = updateinput(x,getinput())
        x = clamp(x, 0, len(options)-1)
        
        if a == 1:
            wait = False
            
    
    return(x)
        

if __name__ == '__main__':
    print("I am a library, not a program")
    print("Use:")
    print("import tui")



    exit()
