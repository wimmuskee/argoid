# -*- coding: utf-8 -*-

from unittest import TestCase
from argoid.config import Configuration

class TestConfiguration(TestCase):
    def test_valid_config(self):
        c = Configuration("client/argoid-client.conf.example","client/argoid-client-conf.schema")
        self.assertEqual(c.config["board"],"beaglebone")

    def test_invalid_config(self):
        with self.assertRaises(RuntimeError):
            c = Configuration("test/invalid-client-config.json","client/argoid-client-conf.schema")

    def test_invalid_config_path(self):
        with self.assertRaises(RuntimeError):
            c = Configuration("test/example-does-not-exist")

