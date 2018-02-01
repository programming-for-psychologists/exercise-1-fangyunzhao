'''
Exercise 1 part 10

@author: Olivia Zhao
'''

import time
import sys
from psychopy import visual,event,core

win = visual.Window([ 400 , 400 ] , color = "black" , units = 'pix') 
square_blue = visual.Rect(win, lineColor="black",
                          fillColor="blue" , size = [ 100 , 100]) 
square_red  = visual.Rect(win, lineColor = 'black',
                          fillColor = 'red', size = [100, 100])

while True:
    square_blue.draw()
    win.flip()
    if event.getKeys(['left']):
        square_blue.size += [10 , 0]
    elif event.getKeys(['right']):
        square_blue.size += [-10 , 0]

   
win.close() 
sys.exit()
