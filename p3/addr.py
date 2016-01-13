import enum
import itertools

from . import at

'''

Defines some addresses, and generates a names dictionary

'''

def MultipleAddress(addressType,args,totalAddresses,addressOffset,nameOffset = 1):
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
        address = address[:-1]

        newArgs = tuple([name,address] + list(args[2:]))
        print(newArgs)
        addressObjects.append(addressType(*newArgs))
    return addressObjects

names = {}


addresses = [
    at.IntegerAddress("playerOnePercent", "804530E0", 16),
    at.IntegerAddress("playerTwoPercent", "80453F70", 16),

    at.IntegerAddress("playerOneStocks", "8045310E", 24),
    at.IntegerAddress("playerTwoStocks", "80453F9E", 24),
    
    at.IntegerAddress("playerOnePercent", "804530E0", 16),
    at.IntegerAddress("playerTwoPercent", "80453F70", 16),
    
    at.IntegerAddress("playerOneChar", "803F0E08", 0, 0xFF),
    at.IntegerAddress("playerTwoChar", "803F0E2C", 0, 0xFF),
    
    at.FloatAddress("playerOneX", "80453090"),
    at.FloatAddress("playerOneY", "80453094"),
    
    at.FloatAddress("playerTwoX", "80453F20"),
    at.FloatAddress("playerTwoY", "80453F24"),
    
    at.IntegerAddress("stageID", "804D6CAD", 16),
    at.IntegerAddress("frameCount", "8046B6CC", 16),
    at.IntegerAddress("currentMenu", "8065CC14", 20, 0xF),

    # at.IntegerAddress("playerOneActionState", "80453130 70"),
    # at.FloatAddress("playerOneDeltaY", "80453130 12C"),
    # at.IntegerAddress("playerOneInAir", "80453130 140"),
    # at.FloatAddress("playerOneHitlagFrames", "80453130 19BC"),
    # at.IntegerAddress("playerOneJumpsUsed", "80453130 19C8", 24),
    # at.FloatAddress("playerOneShieldSize", "80453130 19F8"),
    # at.FloatAddress("playerOneHitstunFrames", "80453130 23A0"),

    # at.IntegerAddress("playerTwoActionState", "80453FC0 70"),
    # at.FloatAddress("playerTwoDeltaY", "80453FC0 12C"),
    # at.IntegerAddress("playerTwoInAir", "80453FC0 140"),
    # at.FloatAddress("playerTwoHitlagFrames", "80453FC0 19BC"),
    # at.IntegerAddress("playerTwoJumpsUsed", "80453FC0 19C8",24),
    # at.FloatAddress("playerTwoShieldSize", "80453FC0 19F8"),
    # at.FloatAddress("playerTwoHitstunFrames", "80453FC0 23A0"),

    at.IntegerAddress("globalFrameCounter", "804D7420"),
]

addresses += MultipleAddress(at.IntegerAddress,("player#Percent", "804530E0", 16) , 4, "E90")

locationsTxt = ""
for address in addresses:
    locationsTxt += address.name + "\n"
    names[address.address] = address