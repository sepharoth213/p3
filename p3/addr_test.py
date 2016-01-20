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
        parsedAddress = False
        for name, value in ao.parse_bytes(struct.pack('>i',123456)):
            # skip over any other parsed addresses, but ensure this one was parsed
            if name == "globalFrameCounter":
                self.assertEqual(value, 123456)
                parsedAddress = True
                
        self.assertTrue(parsedAddress)

    def test_multiple_addresses(self):
        ao = AddressObjects.get_by_address("804C1FAC")
        testInt = (1 << 11) + (1 << 10) + (1 << 9) + (1 << 8)

        parsedAddresses = [False,False,False,False]
        for name, value in ao.parse_bytes(struct.pack('>i', testInt)):
            # skip over any other parsed addresses, but ensure these were parsed
            if name == "controller1Y":
                self.assertTrue(value)
                parsedAddresses[0] = True
            if name == "controller1X":
                self.assertTrue(value)
                parsedAddresses[1] = True
            if name == "controller1B":
                self.assertTrue(value)
                parsedAddresses[2] = True
            if name == "controller1A":
                self.assertTrue(value)
                parsedAddresses[3] = True

        for parsed in parsedAddresses:
            self.assertTrue(parsed)


    def test_accessor(self):
        testMap = {
            "player1X": 3.2,
            "player2InAir": False,
            "player3Stocks": 2,
        }
        AddressObjects.add_multiples_accessors(testMap)

        self.assertEqual(testMap["player"][0].X(),3.2)
        self.assertEqual(testMap["player"][1].InAir(),False)
        self.assertEqual(testMap["player"][2].Stocks(),2)

if __name__ == '__main__':
    unittest.main()
