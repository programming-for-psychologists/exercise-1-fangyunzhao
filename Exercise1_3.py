'''
Exercise 1 part 3

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
square_red.draw() 
win.flip() 
core.wait(1)
square_blue.draw()
win.flip()
core.wait(1)
win.close() 
sys.exit()
