import unittest
import numpy as np

from lightswitch.led import LED

class TestLed(unittest.TestCase):
    
    def setUp(self):
        self.__led = LED(3)
    
    def test_get_grid(self):
        self.assertTrue(np.array_equal(self.__led.get_grid(), [[0, 0, 0], [0, 0, 0], [0, 0, 0]]), "Array does match in get_grid()")
    
    def test_get_status(self):
        self.assertEqual(self.__led.get_status(), 0)

    def test_set_light_status(self):
        self.__led.set_light_status("on", [0, 0, 2, 2])
        self.__led.set_light_status("off", [0, 0, 1, 1])
        self.__led.set_light_status("switch", [1, 1, 2, 2])
        
    def test_get_light_status(self):
        self.assertEqual(self.__led.get_light_status((0, 0)), 0)
    
    
    