from digitalio import DigitalInOut, Direction, Pull
from time import sleep # import other libraries into my library

class rgb():

    def __init__(self, pinR, pinG, pinB):

        self.pinR = DigitalInOut(pinR)
        self.pinR.direction = Direction.OUTPUT

        self.pinG = DigitalInOut(pinG) # setup LED
        self.pinG.direction = Direction.OUTPUT

        self.pinB = DigitalInOut(pinB)
        self.pinB.direction = Direction.OUTPUT

    def red(self):
        self.pinR.value = False
        self.pinG.value = True # how to red
        self.pinB.value = True

    def green(self):
        self.pinR.value = True
        self.pinG.value = False # how to green
        self.pinB.value = True

    def blue(self):
        self.pinR.value = True
        self.pinG.value = True # how to blue
        self.pinB.value = False

    def cyan(self):
        self.pinR.value = True
        self.pinG.value = False # how to cyan
        self.pinB.value = False

    def magenta(self):
        self.pinR.value = False
        self.pinG.value = True # how to magenta
        self.pinB.value = False

    def yellow(self):
        self.pinR.value = False
        self.pinG.value = False # how to yellow
        self.pinB.value = True

    def white(self):
        self.pinR.value = False
        self.pinG.value = False # how to turn all the colors on
        self.pinB.value = False

    def off(self):
        self.pinR.value = True
        self.pinG.value = True # how to turn all the colors off
        self.pinB.value = True

    def rainbow(self, delay):
        self.red()
        sleep(delay)
        self.yellow()
        sleep(delay)
        self.green()
        sleep(delay) # cycle through all the colors
        self.cyan()
        sleep(delay)
        self.blue()
        sleep(delay)
        self.magenta()
        sleep(delay)