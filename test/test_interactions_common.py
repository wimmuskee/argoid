# -*- coding: utf-8 -*-

from unittest import TestCase
from argoid.interactions.interaction import Interaction

class InteractionsCommon(TestCase):
    def test_rolling_average_limit(self):
        i = Interaction()
        for x in range(0,20):
            i.setRollingAverageValue("test",x)
        self.assertEqual(len(i.rolling_averages["test"]), 10)
