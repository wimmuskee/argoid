# -*- coding: utf-8 -*-

from argoid.interactions.interaction import Interaction
import Adafruit_BBIO.GPIO as GPIO
from os.path import isfile
from time import sleep


class BeagleboneInteraction(Interaction):
    def __init__(self):
        Interaction.__init__(self)

    def GpioPollAdc(self,name,gpio,adc):
        """Use provided gpio to power an adc read."""
        self.__setupGPIO(gpio,GPIO.OUT)
        GPIO.output(gpio, GPIO.HIGH)
        sleep(0.2)

        if self.__checkAdcPath(adc):
            value = self.__getPolledAdcRaw(adc)
        else:
            raise RuntimeError("library adc poll not supported yet")

        self.setRollingAverageValue(name,value)
        GPIO.output(gpio, GPIO.LOW)
        self.logger.info(name + "," + str(value))

    def GpioOnAverageBelowThreshold(self,name,sensor_name,gpio,threshold):
        """Check if rolling average for sensor_name is below
        threshold, and engage provided gpio."""
        self.__setupGPIO(gpio,GPIO.OUT)
        if self.checkRollingAverageBelowThreshold(sensor_name,threshold):
            GPIO.output(gpio, GPIO.HIGH)
            self.logger.info(name + "," + str(threshold))
        else:
            GPIO.output(gpio, GPIO.LOW)

    def __setupGPIO(self,gpio,direction):
        try:
            GPIO.setup(gpio,direction)
        except:
            raise

    def __checkAdcPath(self,adc):
        """Provided an adc input, determine if it is a pin number or device path."""
        if adc[0:13] == "/sys/devices/" and isfile(adc):
            return True
        else:
            return False

    def __getPolledAdcRaw(self,adc):
        """Returns polled raw adc value."""
        values = []
        for i in range(1,10):
            with open(adc, "r") as f:
                values.append(int(f.readline().strip()))
        value = sum(values)/len(values)
        return value
