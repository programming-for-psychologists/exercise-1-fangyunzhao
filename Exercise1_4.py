'''
Exercise 1 part 4

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
square_blue.draw() 
win.flip() 
core.wait(1.5)
win.flip()
core.wait(1)
i = 0
while i < 3:
    win.flip()
    square_blue.draw()
    win.flip()
    core.wait(.3)
    i = i + 1
    
    
win.close() 
sys.exit()

