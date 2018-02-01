'''
Exercise 1 part 5

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
win.flip()
i = 1
while i <= 6:
    win.flip()
    core.wait(.5)
    if i % 2 == 0:
        win.flip()
        square_red.draw()
        win.flip()
        core.wait(1)
        i = i + 1
    elif i % 2 != 0:
        win.flip()
        square_blue.draw()
        win.flip()
        core.wait(1)
        i = i + 1
    
    
win.close() 
sys.exit()
