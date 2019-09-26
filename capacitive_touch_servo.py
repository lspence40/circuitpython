import time
import board
import pulseio
from adafruit_motor import servo
import touchio

pwm = pulseio.PWMOut(board.A2, duty_cycle = 2 ** 15, frequency = 50)
my_servo = servo.Servo(pwm)

touch_A0 = touchio.TouchIn(board.A0)
touch_A5 = touchio.TouchIn(board.A5)

angle = 90
speed = 0.2

while True:

    if touch_A0.value:
        angle += speed
    if touch_A5.value:
        angle -= speed
    if angle > 180:
        angle = 180
    if angle < 0:
        angle = 0
    my_servo.angle = angle