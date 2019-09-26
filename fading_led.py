import board
from analogio import AnalogOut

analog_out = AnalogOut(board.A0)

abc = 1
power = 0
speed = 3

while True:

    if(abc):
        power += speed
    else:
        power -= speed

    if(power >= 65000):
        abc = 0
    if(power <= 0):
        abc = 1

    analog_out.value = power