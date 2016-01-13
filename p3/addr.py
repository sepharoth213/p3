import enum

import at

'''

Defines some addresses, and generates a names dictionary

'''

names = {}

addresses = [
    at.IntegerAddress("playerOnePercent", "804530E0", 0x00FF0000, 16),
    at.IntegerAddress("playerTwoPercent", "80453F70", 0x00FF0000, 16),

    at.IntegerAddress("globalFrameCounter", "804D7420", 0xFFFFFFFF, 0),
]

locationsTxt = ""
for address in addresses:
    locationsTxt += address.name + "\n"
    names[address.address] = address