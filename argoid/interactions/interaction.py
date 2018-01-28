# -*- coding: utf-8 -*-

import logging
import logging.handlers


class Interaction:
    def __init__(self):
        self.__setLogger()
        self.rolling_averages = {}

    def setRollingAverageValue(self,name,value):
        if name not in self.rolling_averages:
            self.rolling_averages[name] = []

        # limit number of averages
        if len(self.rolling_averages[name]) == 10:
            del(self.rolling_averages[name][0])

        self.rolling_averages[name].append(value)

    def checkRollingAverageBelowThreshold(self,name,threshold):
        if len(self.rolling_averages[name]) < 10:
            return False

        average = sum(self.rolling_averages[name])/len(self.rolling_averages[name])
        if average < threshold:
            return True
        else:
            return False


    def __setLogger(self):
        handler = logging.handlers.SysLogHandler('/dev/log')
        formatter = logging.Formatter('argoid %(message)s')
        handler.formatter = formatter

        self.logger = logging.getLogger('argoid interaction logger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
