import os
import sys, termios, tty
from .style import styleSet
#style = styleSet("old")

keyarray1 = [['1','2','3','4','5','6','7','8','9','0'],
			 ['q','w','e','r','t','y','u','i','o','p'],
			 ['a','s','d','f','g','h','j','k','l',';'],
			 ['z','x','c','v','b','n','m',' ','.','/']]

keyarray2 = [['1','2','3','4','5','6','7','8','9','0'],
			 ['Q','W','E','R','T','Y','U','I','O','P'],
			 ['A','S','D','F','G','H','J','K','L',':'],
			 ['Z','X','C','V','B','N','M',' ',',','\\']]

keyarray3 = [['!','@','#','$','%','^','&','*','(',')'],
			 ['~',' ',' ',' ','_','+','-','=','{','}'],
			 ['`',' ',' ',' ',',','\"','\'','?','[',']'],
			 [' ',' ',' ',' ',' ',' ','<','>','|',' ']]            
keyarray = [keyarray1,keyarray2,keyarray3]

keystr = ""
x=0
y=0
z=0
a=0
CRED = '\033[44m'
CEND = '\033[0m'



#print("Hello World")
#print(style.tl)



def drawkbdmedium(keyx,keyy, keyarray, width):
	for row in range(0,len(keyarray)):
		print("".join(" " for x in range(0, int(round((width-20)/2)) )), end="")
		for col in range(0,len(keyarray[0])):
			if (col == keyx) & (row == keyy):
				print("[", end="")
			elif (col == keyx+1) & (row == keyy):
				print("", end="")
			else:
				print(" ", end="")
			print(keyarray[row][col], end="")
			if (col == keyx) & (row == keyy):
				print("]", end="")
			else:
				print("", end="")
		print("\n", end="")
	#print()
	
	
def drawkbdsmall(keyx,keyy, keyarray, width):
	for row in range(0,len(keyarray)):
		print("".join(" " for x in range(0, int(round((width-20)/2)) )), end="")
		for col in range(0,len(keyarray[0])):
			if (col == keyx) & (row == keyy):
				print(CRED + keyarray[row][col] + CEND, end="")
			else:
				print(keyarray[row][col], end="")
		print("\n", end="")  

def drawkbdbig(keyx,keyy, keyarray, width):
	for row in range(0,len(keyarray)):
		print("".join(" " for x in range(0, int(round((width-30)/2)) )), end="")
		for col in range(0,len(keyarray[0])):
			if (col == keyx) & (row == keyy):
				print("[", end="")
			else:
				print(" ", end="")
			print(keyarray[row][col], end="")
			if (col == keyx) & (row == keyy):
				print("]", end="")
			else:
				print(" ", end="")
		print("\n", end="")
	
def drawkbdgiant(keyx,keyy, keyarray, width):
	for row in range(0,2*len(keyarray)+1):
		print("".join(" " for x in range(0, int(round((width-30)/2)) )), end="")
		for col in range(0,len(keyarray[0])):
			if row % 2 == 1:
				
				if (col == keyx) & (round(row/2-0.01) == keyy):
					print(u"\u2502", end="")
				else:
					print(" ", end="")
				
				print(keyarray[round(row/2-0.01)][col], end="")
				
				if (col == keyx) & (round(row/2-0.01) == keyy):
					print(u"\u2502", end="")
				else:
					print(" ", end="")
				
			else:
				if (col == keyx):
					if (round(row/2-0.01) == keyy):
						print(u"\u250C", end="")
						print(u"\u2500", end="")
						print(u"\u2510", end="")
					elif (round(row/2-0.01)-1 == keyy) :
						print(u"\u2514", end="")
						print(u"\u2500", end="")
						print(u"\u2518", end="")
				else:
					print("   ", end="")
		print("\n", end="")



def drawtxtbox(title,data,width,styleType = "default"):
	style = styleSet(styleType)
	data=data[-(width-4):]
	print(style.tl, end=" ")
	print(title, end=" ")
	print("".join(style.t for x in range(0,width-2-len(title)-2 )), end="")
	print(style.tr)
	#print("-----------------------------")
	print(style.l, data, end="")
	print(style.c, end="")
	print("".join(" " for x in range(0,(width-4)-len(data))), end="")
	print(style.r)
	print(style.bl, end="")
	print("".join(style.b for x in range(0,width-2)), end="")
	print(style.br)

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


def updateinput(x,y,z,kbd,press):
	a=0
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
		kbd = False
	return(x,y,z,a,kbd)


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
	else:
		press = ""
	return(press)

def kbdinput(title,dispsize,size,keystr,tooltip,getuserinput = getdefaultinput, styleType = "default"):
	global x,y,z,a
	height, width = dispsize
	kbd=True
	if getuserinput == "defaultinput":
		getinput = getdefaultinput
	else:
		getinput = getuserinput
	while kbd == True:
		os.system("clear")
		#x = random.randint(0, len(keyarray[0][0])-1)
		#y = random.randint(0, len(keyarray[0])-1)
		#z = random.randint(0, len(keyarray)-1)
		
		#rows, columns = os.popen('stty size', 'r').read().split()
		#print("start")
		print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")
		drawtxtbox(title, keystr, width, styleType)
		print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")

		if size == "big":
			drawkbdbig(x,y, keyarray[z], width)
		elif size == "medium":
			drawkbdmedium(x,y, keyarray[z], width)
		elif size == "small":
			drawkbdsmall(x,y, keyarray[z], width)
		elif size == "giant":
			drawkbdgiant(x,y, keyarray[z], width)
		
		print("".join("\n" for x in range(0, int(round((height-11)/3)) )), end="")
		print("".join(" " for x in range(0, int(round((width-len(tooltip))/2)) )), end="")
		print(tooltip)
		x,y,z,a,kbd = updateinput(x,y,z,kbd,getinput())
		
		x = clamp(x, 0, len(keyarray[0][0])-1)
		y = clamp(y, 0, len(keyarray[0])-1)
		z = clamp(z, 0, len(keyarray)-1)
		
		if a == 1:
			keystr = keystr + keyarray[z][y][x]
		elif a == -1:
			keystr = keystr[:-1]
	
	return(keystr)
		
