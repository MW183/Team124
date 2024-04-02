from ev3dev2.motor import OUTPUT_D, MoveTank, SpeedRPS, MediumMotor, SpeedPercent
from ev3dev2.sensor.lego import GyroSensor

medMotor = MediumMotor(OUTPUT_D)

medMotor.on_for_degrees(SpeedPercent(100), -45)

