#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port
import time

# Создаем объект EV3Brick для работы с блоком EV3
ev3 = EV3Brick()

lMotor = Motor(Port.B)
rMotor = Motor(Port.C)
sensTwo = ColorSensor(Port.S2)
sensThree = ColorSensor(Port.S3)

robot = DriveBase(lMotor, rMotor, 56.4, 135)

'''
### съезд со зоны старта ###
while sensTwo.reflection() > 60 and sensThree.reflection() > 60:
    robot.straight(10)
robot.stop()

robot.straight(95) 
robot.stop()
'''

c = 2.5
speed = 125


while sensTwo.reflection() > 7.5 or sensThree.reflection() > 7.5: # движение до Т-перекрёстка
    a = sensTwo.reflection()
    b = sensThree.reflection()

    formula = (a-b)*c

    robot.drive(speed, formula)

robot.straight(95) # съезд с Т-перекрёстка

robot.stop()


#robot.turn(79.9) # поворот на 90 градусов



while sensTwo.reflection() > 7.5 or sensThree.reflection() > 7.5: #7-8
    a = sensTwo.reflection()
    b = sensThree.reflection()

    formula = (a-b)*c

    robot.drive(100, formula)

robot.straight(95)
robot.turn(-79.9)

while sensTwo.reflection() > 7.5 or sensThree.reflection() > 7.5: #7-8
    a = sensTwo.reflection()
    b = sensThree.reflection()

    formula = (a-b)*c

    robot.drive(100, formula)

robot.straight(95)
robot.turn(79.9)
while sensTwo.reflection() > 7.5 or sensThree.reflection() > 7.5: #7-8
    a = sensTwo.reflection()
    b = sensThree.reflection()

    formula = (a-b)*c

    robot.drive(100, formula)
'''
robot.straight(95) # съезд с Т-перекрёстка

robot.stop()



robot.stop()

robot.turn(79.9) # поворот на 90 градусов
'''
'''
while not sensTwo.reflection() < 40 and not sensThree.reflection() < 40:
    a = sensTwo.reflection()
    b = sensThree.reflection()

    formula = (a-b)*c

    robot.drive(speed, formula)

robot.stop()
'''