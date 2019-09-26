import time
import board
import neopixel # import required libraries
import adafruit_hcsr04

dot = neopixel.NeoPixel(board.NEOPIXEL, 1) # setup neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3) # setup distance sensor

r = 0
g = 0 # create color variables
b = 0

while True: # loop

    r = 127-(r*6)
    if r > 255:
        r = 255 # calculate amount of red
    if r < 0:
        r = 0
#     print(str(r))

    g *= 10
    if g > 255:
        g *= -1
        g += 512
    if g > 255: # calculate amount of green
        g = 255
    if g < 0:
        g = 0
#     print(str(g))

    b *= 6
    b -= 127
    if b > 255:
        b = 255 # calculate amount of blue
    if b < 0:
        b = 0
#     print(str(b))

    dot.fill((int(r), int(g), int(b))) # make neopixel do RAINBOW

    try:
#         print((sonar.distance))
        r = sonar.distance
        g = sonar.distance # get distance
        b = sonar.distance

    except RuntimeError:
        print("Retrying!")
        r = 0
        g = 0 #what to do if distance is not calculable
        b = 0
        pass

    time.sleep(0.1) # delay for stability

