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

        # TODO: limit number of averages
        self.rolling_averages[name].append(value)


    def __setLogger(self):
        handler = logging.handlers.SysLogHandler('/dev/log')
        formatter = logging.Formatter('argoid %(message)s')
        handler.formatter = formatter

        self.logger = logging.getLogger('argoid interaction logger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
