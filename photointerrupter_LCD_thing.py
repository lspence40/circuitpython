import time
import board
import digitalio
from lcd.lcd import LCD #importing the required libraries
from lcd.lcd import CursorMode
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16) #setup LCD

PI = digitalio.DigitalInOut(board.D8)
PI.direction = digitalio.Direction.INPUT #setup photointerrupter
PI.pull = digitalio.Pull.UP

number = 0
time2 = 0 # variables
now = 0
PIstate = 0

while True:
    now = time.monotonic()
    if now - time2 > 3.999: # do every 4 seconds

        lcd.clear()
        lcd.print("there have been ")
        lcd.print(str(number)) # print # of interruptions
        lcd.print(" interruptions")
        time2 = now

    if PIstate and not PI.value:
        number += 1 # count interruptions
    PIstate = PI.value