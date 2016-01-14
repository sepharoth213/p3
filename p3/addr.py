import enum
import itertools

from p3 import at

'''

Defines some addresses, and generates an addressMap dictionary

'''

def MultipleAddress(addressType,args,addressOffset,totalAddresses = 4,nameOffset = 1):
    addressObjects = []
    namePreSplit, namePostSplit = args[0].split('#')
    baseAddress = [i for i in map(lambda o: int(o, 16), args[1].split())]
    offsets = [i for i in map(lambda o: int(o, 16), addressOffset.split())]
    assert(len(baseAddress) >= len(offsets))
    for i in range(totalAddresses):
        name = namePreSplit + str(i + nameOffset) + namePostSplit
        address = ""
        for b, o in itertools.zip_longest(baseAddress,offsets):
            if o is not None:
                address += hex(b + o*i)[2:] + " "
            else:
                address += hex(b)[2:] + " "
        address = str.upper(address[:-1])

        newArgs = tuple([name,address] + list(args[2:]))
        addressObjects.append(addressType(*newArgs))
    return addressObjects

class AddressObjects:

    def GetByAddress(address):
        return AddressObjects._addressMap[address]

    _addressMap = {}

    allAddressObjects = [
        
        at.IntegerAddress("stageID", "804D6CAD", 16),
        at.IntegerAddress("frameCount", "8046B6CC", 16),
        at.IntegerAddress("currentMenu", "8065CC14", 20, 0xF),

        # at.IntegerAddress("globalFrameCounter", "804D7420"),
    ]

    allAddressObjects += MultipleAddress( at.IntegerAddress, ("player#Percent",     "804530E0", 16),        "E90")
    allAddressObjects += MultipleAddress( at.IntegerAddress, ("player#Stocks",      "8045310E", 24),        "E90")
    allAddressObjects += MultipleAddress( at.IntegerAddress, ("player#Character",   "803F0E08", 0, 0xFF) ,  "14" )
    allAddressObjects += MultipleAddress( at.IntegerAddress, ("player#ActionState", "80453130 70"),         "E90")
    allAddressObjects += MultipleAddress( at.IntegerAddress, ("player#JumpsUsed",   "80453130 19C8",24),    "E90")

    allAddressObjects += MultipleAddress( at.BooleanAddress, ("player#InAir", "80453130 140", "1"), "E90")

    allAddressObjects += MultipleAddress( at.FloatAddress,   ("player#X",             "80453090"),      "E90")
    allAddressObjects += MultipleAddress( at.FloatAddress,   ("player#Y",             "80453094"),      "E90")
    allAddressObjects += MultipleAddress( at.FloatAddress,   ("player#DeltaY",        "80453130 12C"),  "E90")
    allAddressObjects += MultipleAddress( at.FloatAddress,   ("player#HitlagFrames",  "80453130 19BC"), "E90")
    allAddressObjects += MultipleAddress( at.FloatAddress,   ("player#ShieldSize",    "80453130 19F8"), "E90")
    allAddressObjects += MultipleAddress( at.FloatAddress,   ("player#HitstunFrames", "80453130 23A0"), "E90")

    locationsTxt = ""
    for address in allAddressObjects:
        locationsTxt += address.address + "\n"
        _addressMap[address.address] = address
