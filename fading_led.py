import board #libraries
from analogio import AnalogOut

analog_out = AnalogOut(board.A0) #setup LED

abc = 1 #variables
power = 0
speed = 3

while True: #repeat

    if(abc):
        power += speed #power goes up
    else:
        power -= speed #and also down

    if(power >= 65000):
        abc = 0
    if(power <= 0): #this is the thing that decides whether power goes up or down
        abc = 1

    analog_out.value = power #run power through the LED
