from digitalio import DigitalInOut, Direction, Pull #pylint: disable-msg=import-error
from time import sleep # import other libraries into my library

class FancyLED():

    def __init__(self, pin1, pin2, pin3):
        self.pin1 = DigitalInOut(pin1)
        self.pin1.direction = Direction.OUTPUT

        self.pin2 = DigitalInOut(pin2) # setup LED
        self.pin2.direction = Direction.OUTPUT

        self.pin3 = DigitalInOut(pin3)
        self.pin3.direction = Direction.OUTPUT

    def alternate(self):
        for i in range(0, 3, 1):
            self.pin1.value = False
            self.pin2.value = True # how to alternate
            self.pin3.value = False
            sleep(.5)
            self.pin1.value = True
            self.pin2.value = False
            self.pin3.value = True
            sleep(.5)
            i = i

    def blink(self):
        for i in range(0, 2, 1):
            self.pin1.value = True
            self.pin2.value = True # how to blink
            self.pin3.value = True
            sleep(.75)
            self.pin1.value = False
            self.pin2.value = False
            self.pin3.value = False
            sleep(.75)
            i = i

    def chase(self):
        for i in range(0, 5, 1):
            self.pin1.value = True
            self.pin2.value = False # how to chase
            self.pin3.value = False
            sleep(.1)
            self.pin1.value = False
            self.pin2.value = True
            self.pin3.value = False
            sleep(.1)
            self.pin1.value = False
            self.pin2.value = False
            self.pin3.value = True
            sleep(.1)
            i = i

    def sparkle(self):
        for i in range(0, 15, 1):
            self.pin1.value = False
            self.pin2.value = True # how to sparkle
            self.pin3.value = False
            sleep(.1)
            self.pin1.value = True
            self.pin2.value = False
            self.pin3.value = True
            sleep(.1)
            i = i