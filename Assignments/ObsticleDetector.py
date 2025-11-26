#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the EV3 Brick.
ev3 = EV3Brick()

obstacle_sensor = UltrasonicSensor(port=Port.S3)
touch_sensor = TouchSensor(port=Port.S2)
left_motor = Motor(port=Port.B)
right_motor = Motor(port=Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

value = False

while not value:
    if touch_sensor.pressed():
        value = True

ev3.speaker.beep()
ev3.speaker.say("Exercise two")

while value:
    # Begin driving forward at 200 millimeters per second.
    robot.drive(200, 0)

    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing (waiting for 10 milliseconds) while the measured
    # distance is still greater than 300 mm.
    while obstacle_sensor.distance() < 300:
        wait(10)
        robot.straight(-150)
        robot.turn(35)

    if touch_sensor.pressed():
        robot.drive(0,0)
        ev3.speaker.say("Exercise done")
        #wait for 50 milliseconds
        #value 1
        value = False
        ev3.stop()