#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_greater(self):
        list = [5, 1, 10, 3]
        self.assertEqual(max_integer(list), 10)

    def test_uniq(self):
        list = [10]
        self.assertEqual(max_integer(list), 10)
        
    def test_dual(self):
        list = [10, 5]
        self.assertEqual(max_integer(list), 10)
    
    def test_mirror(self):
        list = [10, 10]
        self.assertEqual(max_integer(list), 10)
    
    def test_empty(self):
        list = []
        self.assertIsNone(max_integer(list))
    
    def test_str(self):
        list = ["simon"]
        self.assertEqual(max_integer(list), "simon")
    
    def test_negative(self):
        list=[-1, -12, -10, -100, 6]
        self.assertEqual(max_integer(list), 6)
        
    def test_float(self):
        list=[3.667, 3.668]
        self.assertEqual(max_integer(list), 3.668)

    def test_is_list(self):
        data=[3.667, 3.668]
        self.assertIsInstance(data, list)
    
    def test_is_int_or_float(self):
        data=[3, 3.668]
        for i in range(len(data)):
            self.assertIsInstance(data[i], (int, float))
    
    
    
        
    
        
    
