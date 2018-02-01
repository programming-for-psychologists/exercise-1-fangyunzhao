'''
Exercise 1 part 12

@author: Olivia Zhao
'''

import time
import sys
from psychopy import visual,event,core
from operator import pos

win = visual.Window([ 400 , 400 ] , color = "black" , units = 'pix') 
square_blue = visual.Rect(win, lineColor="black",
                          fillColor="blue" , size = [100 , 100],
                          pos = [100, 0]) 
square_red  = visual.Rect(win, lineColor = 'black',
                          fillColor = 'red', size = [100, 100],
                          pos = [-100, 0])
while True:
    square_red.ori += 10
    square_blue.ori += -10
    square_red.draw()
    square_blue.draw()
    win.flip()

   
win.close() 
sys.exit()
