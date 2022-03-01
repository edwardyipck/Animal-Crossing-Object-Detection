import pyautogui as pg
import time
import mss
import mss.tools
from greenscreen_photo import *

from PIL import ImageGrab
m = 2

folder = r"D:\Current Work\Python\PROJECTS\Animal Crossing image processing\output photos"

def photo(e,a,n):
    co = [[1180,560,1460,840],[1160,580,1490,950],[1140,620,1520,1100]]
   
    snapshot = ImageGrab.grab(bbox = co[a])
    # snapshot.save(folder+"\\GREEEN " + str(e) + "-" + str(a) + "-" + str(n) + ".png")
    photo = removegreen(snapshot)
    cv2.imwrite(folder+"\\photo " + str(e) + "-" + str(a) + "-" + str(n) + ".png", photo)
    
# Vsync
def vsync():
    pg.click(x=120, y=1428)

def shirt():
    pg.keyDown('t')
    pg.keyUp('t') 
    time.sleep(0.5)
    pg.keyDown('d')
    pg.keyUp('d') 
    pg.keyDown('d')
    pg.keyUp('d') 
    pg.keyDown('h')
    pg.keyUp('h') 
    pg.keyDown('[')
    pg.keyUp('[')
    time.sleep(0.5)
    
# Sets villager in the middle
def middleset():
    with pg.hold('h'):
        time.sleep(0.1)
        pg.keyDown('a') 
        time.sleep(0.01)
        pg.keyUp('a')
        time.sleep(0.01)
        pg.keyDown('w')
        time.sleep(0.01)
        pg.keyUp('w')
        
# Cursor Movement
def cursoraway(v):
    pg.keyDown('s')
    if v == 0:
        pg.keyDown('a') 
    time.sleep(0.6)
    pg.keyUp('s')
    pg.keyUp('a') 

# unused
def cursorback():
    pg.keyDown('w')
    pg.keyDown('d') 
    time.sleep(0.25)
    pg.keyUp('w')
    pg.keyUp('d')

# Spins the camera
def cameraspin(e,a,d):
    time.sleep(0.3)
    
    if d == 0:
        key = "j"
    else:
        key = "l"
    
    for n in range(16):
        pg.keyDown(key)
        time.sleep(0.0065)
        pg.keyUp(key)
        photo(e,a,n)


# Moves the camera down
def cameradown(n):
    for i in range(n):
        pg.keyDown('i')
        pg.keyUp('i')

def resetcamera():
    pg.keyDown('[')
    pg.keyUp('[')
    time.sleep(0.5)
    pg.keyDown('[')
    pg.keyUp('[')

def roommove(mode):
    
    if mode == 0:
        pg.keyDown('[')
        pg.keyUp('[')
        time.sleep(0.35)
        pg.keyDown('j')
        pg.keyUp('j')
        time.sleep(0.35)
        pg.keyDown('[')
        pg.keyUp('[')
        
    if mode == 1:
        pg.keyDown('[')
        pg.keyUp('[')
        time.sleep(0.35)
        pg.keyDown('j')
        pg.keyUp('j')
        time.sleep(0.35)
        pg.keyDown('j')
        pg.keyUp('j')
        time.sleep(0.35)
        pg.keyDown('[')
        pg.keyUp('[')


# Runs back into view and presses inventory
def runback(mode):
    if mode == 0:
        with pg.hold('g'):
            pg.keyDown('s')
            pg.keyDown('d') 
            time.sleep(0.5)
            pg.keyUp('s')
            pg.keyUp('d')
        pg.keyDown('x')
        pg.keyUp('x')
    
    if mode == 1:
        with pg.hold('g'):
            pg.keyDown('s')
            pg.keyDown('a') 
            time.sleep(0.8)
            pg.keyUp('s')
            pg.keyUp('a')
        pg.keyDown('x')
        pg.keyUp('x')
    
# Selects emotion [up,down,right]
def emotion(x):
    move = [[0,1,1],[1,0,2],[0,0,3]]
    pg.keyDown('3')
    pg.keyUp('3')
    time.sleep(1)
    for i in range(move[x][0]):
        pg.keyDown('w')
        pg.keyUp('w')
    for i in range(move[x][1]):
        pg.keyDown('s')
        pg.keyUp('s')
    for i in range(move[x][2]):
        pg.keyDown('d')
        pg.keyUp('d')
    pg.keyDown('h')
    pg.keyUp('h')
    
def emotionreset():
    pg.keyDown('3')
    pg.keyUp('3')
    time.sleep(0.3)
    for i in range(2):
        pg.keyDown('w')
        pg.keyDown('a')
        time.sleep(0.2)
        pg.keyUp('w')
        pg.keyUp('a')
    pg.keyDown('h')
    pg.keyUp('h')
    
def amiiboselect(x):
    time.sleep(m)
    pg.keyDown('F10')
    pg.keyUp('F10')
    for i in range(2):
        pg.keyDown('right')
        pg.keyUp('right')
    time.sleep(0.5)
    for i in range(4):
        pg.keyDown('down')
        time.sleep(0.2)
        pg.keyUp('down')
    pg.keyDown('enter')
    time.sleep(0.2)
    pg.keyUp('enter') 
    time.sleep(0.8)
    for i in range(5): 
        pg.keyDown('tab')
        pg.keyUp('tab')
    for i in range(x): 
        pg.keyDown('down')
        time.sleep(0.1)
        pg.keyUp('down')
    for i in range(3): 
        pg.keyDown('tab')
        pg.keyUp('tab')    
    pg.keyDown('enter')
    time.sleep(0.2)
    pg.keyUp('enter')
    
