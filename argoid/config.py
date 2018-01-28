# -*- coding: utf-8 -*-

import json
from time import time

class Configuration:
    def __init__(self):
        with open("/etc/argoid/argoid-client.conf") as f:
            self.config = json.loads(f.read())

        # also validate

        # set initial and recurring time for all interactions
        for interaction_name in self.config["interactions"]:
            self.config["interactions"][interaction_name]["timestamp"] = round(time())

    def getActionTime(self,interaction):
        return self.config["interactions"][interaction]["timestamp"] + self.config["interactions"][interaction]["recurring"]

    def setTimestamp(self,interaction,timestamp):
        self.config["interactions"][interaction]["timestamp"] = timestamp
