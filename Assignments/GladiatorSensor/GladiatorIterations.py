#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random
import time
from threading import Thread

ev3 = EV3Brick()
color_sensor= ColorSensor(port=Port.S4)
obstacle_sensor = UltrasonicSensor(port=Port.S3)
touch_sensor = TouchSensor(port=Port.S2)

left_motor = Motor(port=Port.B)
right_motor = Motor(port=Port.C)
my_motor = Motor(port=Port.A)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)
def function():
    my_motor.run(0)
    valg = random.randrange(1,5)
    if(valg == 1):
        ev3.screen.print("function 1")
        my_motor.run(-1000)
        wait(10)

    elif(valg == 2):
        ev3.screen.print("function 2")
        robot.drive(0,0)
        robot.turn(355)
        robot.turn(-355)
        wait(10)

    elif(valg == 3):
        ev3.screen.print("function 3")
        robot.drive(0,0)
        ev3.speaker.play_file(SoundFile.T_REX_ROAR)
        ev3.speaker.play_file(SoundFile.T_REX_ROAR)
        ev3.speaker.play_file(SoundFile.T_REX_ROAR)
        ev3.speaker.play_file(SoundFile.T_REX_ROAR)
        
    else:
        ev3.screen.print("function 4") 
        robot.drive(0,0)
        ev3.screen.print("Are you not entertained?")
        ev3.speaker.say("Are you not entertained?")
        ev3.speaker.say("Are you not entertained?")
        ev3.speaker.say("Is this not why you're here?")
        wait(10)
        
value = False
while not value:
    if touch_sensor.pressed():
        value = True
ev3.speaker.beep()
ev3.speaker.say("Exercise three")
index = 0
j = 0
while value:
    if color_sensor.reflection() <= 28:
        robot.drive(40, 20)
    else:
        robot.drive(40, -40)

    if j > 5000: #Egt 20000
        function()
        j = 0
    j += 1

    if obstacle_sensor.distance() < 200:
        robot.drive(0,0)
        ev3.speaker.play_file(SoundFile.FANFARE)
        ev3.stop()

    if touch_sensor.pressed():
        robot.drive(0,0)
        ev3.speaker.say("Exercise done")
        #wait for 50 milliseconds
        #value 1
        value = False
        ev3.stop()
