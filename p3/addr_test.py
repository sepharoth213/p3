import os
import socket
import unittest
import struct

from p3.addr import AddressObjects
from p3.at import IntegerAddress

class AddressesTest(unittest.TestCase):

    def addressEqual(self,a,b):
        self.assertEqual(a.name,b.name)
        self.assertEqual(a.address,b.address)
        self.assertEqual(a.shift,b.shift)
        self.assertEqual(a.mask,b.mask)

    def test_integer(self):
        test1 = [
                IntegerAddress("t1est", "DEADBEE0"),
                IntegerAddress("t2est", "DEADBEE1"),
                IntegerAddress("t3est", "DEADBEE2"),
            ]

        test2 = [
                IntegerAddress("test1", "DEADBE00", 16),
                IntegerAddress("test2", "DEADBE12", 16),
                IntegerAddress("test3", "DEADBE24", 16),
                IntegerAddress("test4", "DEADBE36", 16),
            ]

        test3 = [
                IntegerAddress("3test", "DEADBEE0 0", 20, 0xF),
                IntegerAddress("4test", "DEADBEE0 11", 20, 0xF),
                IntegerAddress("5test", "DEADBEE0 22", 20, 0xF),
                IntegerAddress("6test", "DEADBEE0 33", 20, 0xF)
            ]
        m1 = AddressObjects._multiple_address(IntegerAddress,("t#est","DEADBEE0"),"1",3)
        m2 = AddressObjects._multiple_address(IntegerAddress,("test#","DEADBE00", 16),"12")
        m3 = AddressObjects._multiple_address(IntegerAddress,("#test","DEADBEE0 0", 20, 0xF),"0 11",4,3)

        for i in range(len(test1)):
            self.addressEqual(test1[i],m1[i])
        for i in range(len(test2)):
            self.addressEqual(test2[i],m2[i])
        for i in range(len(test3)):
            self.addressEqual(test3[i],m3[i])

if __name__ == '__main__':
    unittest.main()
