import os
import sys, termios, tty
import time
from .style import styleSet

x=0
selected=""


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

def updateinput(x,a,listing,press):
    if press =="up":
        x=x-1
    elif press == "down":
        x=x+1
    elif press == "select":
        a=1
    elif press == "exit":
        listing = False
    return(x,a,listing)


def getdefaultinput():
    char = getch()
    if (char == "q"):
        press = "exit"
    elif (char == "s"):
        press = "down"
    elif (char == "w"):
        press = "up"
    elif (char == "e"):
        press = "select"
    return(press)


def drawlistbox(title,options,width,height,x,styleType):
    style = styleSet(styleType)
    print(style.tl, end=" ")
    print(title, end=" ")
    print("".join(style.t for x in range(0,width-2-len(title)-2 )), end="")
    print(style.tr)
    #print("-----------------------------")
    i=0
    for option in options:
        print(style.l, end="")
        if x == i:
             print(" > ", end="")
        else:
            print("   ", end="")
        i=i+1
        if i < height-2:
            print(str(option), end="")
            print("".join(" " for x in range(0,(width-5)-len(str(option)))), end="")
            print(style.r)
        else:
            print("<...>",end="")
            print("".join(" " for x in range(0,(width-10))), end="")
            print(style.r)
            break
        #print(u'\u2588', end="")

    for i in range(0,(height - len(options) - 2)):
        print(style.l, end="")
        print("".join(" " for x in range(0,(width-2))), end="")
        print(style.r)

    print(style.bl, end="")
    print("".join(style.b for x in range(0,width-2)), end="")
    print(style.br)


def listselect(title,dispsize,options,size,tooltip,getuserinput="defaultinput",styleType = "default"):
    global x
    height, width = dispsize
    listing=True
    selected=""
    a=0
    if getuserinput == "defaultinput":
        getinput = getdefaultinput
    else:
        getinput = getuserinput
    while listing == True:
        os.system("clear")

        drawlistbox(title, options, width,height-2,x,styleType)       
        print("".join(" " for x in range(0, int(round((width-len(tooltip))/2)) )), end="")
        print(tooltip)

        x,a,listing = updateinput(x,a,listing,getinput())
        x = clamp(x, 0, len(options)-1)
        
        if a == 1:
            selected = options[x]
            listing = False
        #elif a == -1:
        #    keystr = keystr[:-1]
    
    return(selected)


if __name__ == '__main__':
    print("I am a library, not a program")
    print("Use:")
    print("import tui")

    options = ["first","second","third"]
    t = listselect("Select one:",(40,40),options,"small","tooltip",styleType="default")

    exit()
