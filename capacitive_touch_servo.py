import time
import board
import pulseio #libraries
from adafruit_motor import servo
import touchio

pwm = pulseio.PWMOut(board.A2, duty_cycle = 2 ** 15, frequency = 50)
my_servo = servo.Servo(pwm) #prepare servo

touch_A0 = touchio.TouchIn(board.A0)
touch_A5 = touchio.TouchIn(board.A5) #prepare touchable wire thingies

angle = 90 #variables
speed = 0.2

while True: #repeat forever

    if touch_A0.value:
        angle += speed #go one way
        
    if touch_A5.value:
        angle -= speed #go the other way
        
    if angle > 180:
        angle = 180
    if angle < 0: #constrain angle
        angle = 0
        
    my_servo.angle = angle #move the servo to the designated position
