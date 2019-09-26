import RGB # my library

import board
import time # other libraries

r1 = board.D2
g1 = board.D3 # setup LED1
b1 = board.D4
myRGB1 = RGB.rgb(r1, g1, b1)

r2 = board.D5
g2 = board.D6 # setup LED2
b2 = board.D7
myRGB2 = RGB.rgb(r2, g2, b2)

myRGB2.off()
myRGB1.off() # reset

while True:

    myRGB1.off()
    myRGB2.red() # red slides on
    time.sleep(1)

    for i in range(0, 2, 1): # do color slidy thing twice

        myRGB1.red()
        myRGB2.yellow()
        time.sleep(1)

        myRGB1.yellow()
        myRGB2.green()
        time.sleep(1)

        myRGB1.green()
        myRGB2.cyan()
        time.sleep(1)

        myRGB1.cyan()
        myRGB2.blue()
        time.sleep(1)

        myRGB1.blue()
        myRGB2.magenta()
        time.sleep(1)

        myRGB1.magenta()
        myRGB2.red()
        time.sleep(1)

    myRGB1.red()
    myRGB2.off()
    time.sleep(1) # red slides off
    myRGB1.off()
    time.sleep(1)

    myRGB2.rainbow(1)
    myRGB2.off() # do first ranbow, slowly

    for i in range(0,4,1): # do 4 times

        myRGB1.rainbow(.2)
    myRGB1.off() # do second rainbow, quickly
    time.sleep(1)