import os
import socket
import unittest
import struct

from p3.at import IntegerAddress
from p3.at import FloatAddress
from p3.at import BooleanAddress

class AddressTypeTest(unittest.TestCase):

    def test_integer(self):
        test1 = IntegerAddress("test", "DEADBEEF")
        test2 = IntegerAddress("test", "DEADBEEF", 16)
        test3 = IntegerAddress("test", "DEADBEEF", 20, 0xF)

        self.assertEqual(test1.parse_bytes(b'\x00\x00\x01\x02'),258)
        self.assertEqual(test1.parse_bytes(b'\x00\x01\x01\x04'),65796)
        self.assertEqual(test1.parse_bytes(b'\x10\x01\x01\x00'),268501248)
        self.assertEqual(test2.parse_bytes(b'\x00\x00\x31\x00'),0)
        self.assertEqual(test2.parse_bytes(b'\x00\x01\x01\x20'),1)
        self.assertEqual(test2.parse_bytes(b'\x01\x01\x01\x00'),257)
        self.assertEqual(test3.parse_bytes(b'\x00\x00\x31\x00'),0)
        self.assertEqual(test3.parse_bytes(b'\x00\x11\x01\x00'),1)
        self.assertEqual(test3.parse_bytes(b'\x01\xA1\x01\x00'),10)

    def test_float(self):
        test = FloatAddress("test", "DEADBEEF")

        self.assertEqual(test.parse_bytes(struct.pack('f', 2)),2)
        self.assertEqual(test.parse_bytes(struct.pack('f', 1923102)),1923102)
        self.assertEqual(round(test.parse_bytes(struct.pack('f', 121.1231)),4),121.1231)
        
    def test_bool(self):
        test1 = BooleanAddress("test", "DEADBEEF", "10")
        test2 = BooleanAddress("test", "DEADBEEF", "4", 16)
        test3 = BooleanAddress("test", "DEADBEEF", "8", 20, 0xF)

        self.assertEqual(test1.parse_bytes(b'\x40\x02\x01\x02'),False)
        self.assertEqual(test1.parse_bytes(b'\x00\x00\x00\x10'),True)
        self.assertEqual(test2.parse_bytes(b'\x13\x16\x31\xFF'),False)
        self.assertEqual(test2.parse_bytes(b'\x00\x04\x31\xFF'),True)
        self.assertEqual(test3.parse_bytes(b'\x10\x25\x31\x00'),False)
        self.assertEqual(test3.parse_bytes(b'\x4A\x81\x01\xBB'),True)

if __name__ == '__main__':
    unittest.main()
