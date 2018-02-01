'''
Exercise 1 part 9

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

a = 10
while True:
    square_red.ori += a
    square_red.draw()
    win.flip()
    if event.getKeys(['s']):
        a = 0
    elif event.getKeys(['r']):
        a = 10

   
win.close() 
sys.exit()