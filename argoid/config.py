# -*- coding: utf-8 -*-

from os.path import isfile
import json
from jsonschema import validate
from time import time

class Configuration:
    def __init__(self,
        configpath="/etc/argoid/argoid-client.conf",
        schemapath="/usr/share/argoid/argoid-client-conf.schema"):

        if not isfile(configpath):
            raise RuntimeError("cannot find client configuration at " + configpath)

        with open(configpath) as f:
            self.config = json.loads(f.read())

        with open(schemapath) as f:
            schema = json.loads(f.read())

        try:
            validate(self.config, schema)
        except:
            raise RuntimeError("error validating configuration against schema: " + schemapath)

        # set initial time for all interactions
        for interaction_name in self.config["interactions"]:
            self.config["interactions"][interaction_name]["timestamp"] = round(time()) + self.config["interactions"][interaction_name]["offset"]

    def getActionTime(self,interaction):
        return self.config["interactions"][interaction]["timestamp"] + self.config["interactions"][interaction]["recurring"]

    def setTimestamp(self,interaction,timestamp):
        self.config["interactions"][interaction]["timestamp"] = timestamp
