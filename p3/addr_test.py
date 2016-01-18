import os
import socket
import unittest
import struct

from p3.addr import AddressObjects

class AddressesTest(unittest.TestCase):
    def setUp(self):
        AddressObjects.init()

    def test_accessor(self):
        kek = AddressObjects._name_map["player1X"];
        print(kek)
        kek = AddressObjects._name_map["player"][0].X();
        print(repr(kek));
        self.assertEqual(kek.name,"player1X")
        # self.assertEqual(AddressObjects["player"][0]address,b.address)
        # self.assertEqual(AddressObjects["player"][0]shift,b.shift)
        # self.assertEqual(AddressObjects["player"][0]mask,b.mask)

if __name__ == '__main__':
    unittest.main()
