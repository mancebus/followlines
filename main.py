#!/usr/bin/env pybricks-micropython
import time
import sys
import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from controller import ControllerPID

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

class LineFollower:

    def __init__(self,controller):
        self.leftMotor = Motor(Port.B,positive_direction=Direction.COUNTERCLOCKWISE)
        self.rightMotor = Motor(Port.C,positive_direction=Direction.COUNTERCLOCKWISE)
        self.lightSensor = ColorSensor(Port.S3)
        self.controller = controller

    def run(self):
        while True:
            light = self.lightSensor.reflection()
            left,right = self.controller.getPower(float(light))
            message = 'Z:%d L:%d R:%d' % (light,left,right)
            ev3.screen.print(message)
            self.leftMotor.run(left)
            self.rightMotor.run(right)
        

ev3 = EV3Brick()

def log(msg):
    # prueba
    ev3.screen.print(msg)
    time.sleep(2.0)

Tp = 200.0

whiteValue = 76.0
blackValue = 6.0

controller = ControllerPID(whiteValue,blackValue,Tp)
log('INIT')

lf = LineFollower(controller)
lf.run()

#scp robot@ev3dev.local:/home/robot/LineFollower/data.csv .

