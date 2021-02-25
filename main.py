#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
ev3.speaker.set_speech_options("en", "m1")
remote = InfraredSensor(Port.S3)
left = Motor(Port.A)
right = Motor(Port.B)
drive = DriveBase(left, right, 62, 154)
rack = Motor(Port.C)

FORWARD = set([Button.LEFT_UP, Button.RIGHT_UP])
BACKWARD = set([Button.LEFT_DOWN, Button.RIGHT_DOWN])
LEFT = set([Button.LEFT_UP])
RIGHT = set([Button.RIGHT_UP])
STOP = set([Button.BEACON])
RACK_UP = set([Button.LEFT_DOWN])
RACK_DOWN = set([Button.RIGHT_DOWN])

def run_remote_mode():
    buttons = set(remote.buttons(1))
    if buttons == FORWARD:
        drive.drive(2000, 0)
    elif buttons == BACKWARD:
        drive.drive(-2000, 0)
    elif buttons == LEFT:
        drive.stop()
        wait(50)
        drive.turn(-10)
    elif buttons == RIGHT:
        drive.stop()
        wait(50)
        drive.turn(10)
    elif buttons == STOP: 
        drive.stop()
    elif buttons == RACK_UP:
        rack.run_angle(45, -10)
    elif buttons == RACK_DOWN:
        rack.run_angle(45, 10)

ev3.speaker.say("Hello! You may control me.")
ev3.screen.clear()
while True:
    run_remote_mode()