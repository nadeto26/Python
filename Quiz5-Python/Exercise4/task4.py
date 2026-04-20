import unittest

def magic(op1, op2, operation):
    try:
        if operation == '/':
            return op1 / op2
        else:
            return op1 + op2
    except ZeroDivisionError:
        return 0
    except Exception:
        raise

from unittest import TestCase, main

class Test(TestCase):
    def test1(self):
        self.assertEqual(magic(2, 2, '/'), 1)

    def test2(self):
        self.assertEqual(magic(2, 2, '+'), 4)

    def zero_error(self):
        with self.assertRaises(ZeroDivisionError):
            magic(0, 0, '/')

    def test4(self):
        with self.assertRaises(Exception):
            magic(13, "xx", "+")


