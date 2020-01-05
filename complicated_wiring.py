from fancyLED import FancyLED #imports my custom library

fancy1 = FancyLED(2,3,4)
fancy2 = FancyLED(5,6,7) #sets up LEDs

while True:
    fancy1.alternate()
    fancy2.blink() #uses the library
    fancy1.chase()
    fancy2.sparkle()
