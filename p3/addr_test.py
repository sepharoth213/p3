import unittest
import struct

from p3.addr import AddressObjects

class AddressesTest(unittest.TestCase):
    def setUp(self):
        AddressObjects.init()

    def test_by_name(self):
        ao = AddressObjects.get_by_name("globalFrameCounter")
        self.assertEqual(ao.parse_bytes(struct.pack('>i',123456)), 123456)

    def test_by_address(self):
        ao = AddressObjects.get_by_address("80479D60")
        self.assertEqual(ao.parse_bytes(struct.pack('>i',123456)), 123456)

    def test_accessor(self):
        testMap = {
            "player1X": 3.2,
            "player2DeltaY": 6.4,
            "player3Stocks": 2,
        }
        AddressObjects.add_multiples_accessors(testMap)

        self.assertEqual(testMap["player"][0].X(),3.2)
        self.assertEqual(testMap["player"][1].DeltaY(),6.4)
        self.assertEqual(testMap["player"][2].Stocks(),2)

if __name__ == '__main__':
    unittest.main()
