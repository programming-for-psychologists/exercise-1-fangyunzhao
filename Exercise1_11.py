'''
Exercise 1 part 11

@author: Olivia Zhao
'''

import time
import sys
from psychopy import visual,event,core

win = visual.Window([ 400 , 400 ] , color = "black" , units = 'pix') 
x = 100
y = 100

while True:
    square_blue = visual.Rect(win, lineColor="black",
                          fillColor="blue" , size = [ x , y]) 
    square_blue.draw()
    win.flip()
    if event.getKeys(['left']):
        x = 1.1 * x
    elif event.getKeys(['right']):
        x = 0.9 * x

   
win.close() 
sys.exit()
