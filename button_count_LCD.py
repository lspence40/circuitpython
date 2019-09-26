import board
import digitalio
from lcd.lcd import LCD #importing the required libraries
from lcd.lcd import CursorMode
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16) #setup LCD

button = digitalio.DigitalInOut(board.D8)
button.direction = digitalio.Direction.INPUT #setup button
button.pull = digitalio.Pull.DOWN

switch = digitalio.DigitalInOut(board.D5)
switch.direction = digitalio.Direction.INPUT #setup switch
switch.pull = digitalio.Pull.DOWN

upDown = 1
buttonState = 0 #create variables
number = 0

while True: #loop

    if not buttonState and button.value:
        number += upDown #count when button is pressed
    buttonState = button.value

    if switch.value:
        upDown = 1 #should the number go up or down?
    else:
        upDown = -1

    lcd.set_cursor_pos(0, 0)
    lcd.print("up or down: ")
    if upDown == 1:
        lcd.print("up  ") #print things to LCD
    else:
        lcd.print("down")
    lcd.print("number is: ")
    lcd.print(str(number))
    lcd.print("    ")