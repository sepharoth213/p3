import enum
import itertools

from p3 import at

'''

Defines some addresses, and generates an addressMap dictionary

'''

class AddressObjects:

    address_objects = [
        
        at.IntegerAddress("stageID", "804D6CAD", 16),
        at.IntegerAddress("frameCount", "8046B6CC", 16),
        at.IntegerAddress("currentMenu", "8065CC14", 20, 0xF),

        at.IntegerAddress("globalPowerOnCounter", "804D7420"),
        at.IntegerAddress("globalFrameCounter", "80479D60"),
    ]

    @classmethod
    def init(cls):
        cls._add_multiple("player", 4, 1)
        cls._add_multiple("controller", 4, 1)

        cls._multiple_address("player", "Percent",     at.IntegerAddress, ("804530E0", 16),        "E90")
        cls._multiple_address("player", "Stocks",      at.IntegerAddress, ("8045310E", 24),        "E90")
        cls._multiple_address("player", "Character",   at.IntegerAddress, ("803F0E08 ", 0, 0xFF) ,  "14" )
        cls._multiple_address("player", "ActionState", at.IntegerAddress, ("80453130 70"),         "E90")
        cls._multiple_address("player", "JumpsUsed",   at.IntegerAddress, ("80453130 19C8",24),    "E90")

        cls._multiple_address("player", "InAir", at.BooleanAddress, ("80453130 140", "1"), "E90")

        cls._multiple_address("player", "X",              at.FloatAddress, ("80453090"),      "E90")
        cls._multiple_address("player", "Y",              at.FloatAddress, ("80453094"),      "E90")
        cls._multiple_address("player", "AnimationSpeed", at.FloatAddress, ("80453130 8FC"),  "E90")
        cls._multiple_address("player", "Facing",         at.FloatAddress, ("80453130 8C"),   "E90")
        cls._multiple_address("player", "DeltaY",         at.FloatAddress, ("80453130 12C"),  "E90")
        cls._multiple_address("player", "HitlagFrames",   at.FloatAddress, ("80453130 19BC"), "E90")
        cls._multiple_address("player", "ShieldSize",     at.FloatAddress, ("80453130 19F8"), "E90")
        cls._multiple_address("player", "HitstunFrames",  at.FloatAddress, ("80453130 23A0"), "E90")

    @classmethod
    def _add_multiple(cls,name,numMultiples,nameOffset):
        cls._multiples[name] = _Multiple(name,numMultiples,nameOffset)

    @classmethod
    def _multiple_address(cls,multipleName,field,addressType,args,addressOffset):
        if not isinstance(args, tuple):
            args = (args,)
        baseAddress = [i for i in map(lambda o: int(o, 16), args[0].split())]
        offsets = [i for i in map(lambda o: int(o, 16), addressOffset.split())]
        multiple = cls._multiples[multipleName]

        assert(len(baseAddress) >= len(offsets))

        for i in range(multiple.numMultiples):
            name = multipleName + multiple.identifiers[i] + field
            address = ""
            for b, o in itertools.zip_longest(baseAddress,offsets):
                if o is not None:
                    address += hex(b + o*i)[2:] + " "
                else:
                    address += hex(b)[2:] + " "

            #remove trailing space
            address = str.upper(address[:-1])

            newArgs = tuple([name,address] + list(args[1:]))
            cls.address_objects.append(addressType(*newArgs))

            locations_txt = ""
            for address in cls.address_objects:
                locations_txt += address.address + "\n"
                cls._address_map[address.address] = address

    @classmethod
    def get_by_address(cls,address):
        return cls._address_map[address]

    @classmethod
    def add_multiples_accessors(cls,addressDict):
        for key, multiple in cls._multiples:
            addressDict[multiple.name] = {}
            instance = {}
            for i in multiple.identifiers:
                addressDict[multiple.name][i] = _Empty()
                for member in multiple.members:
                    setattr(addressDict[multiple.name][i], member, lambda: addressDict[multiple.name + str(i) + member])

    _address_map = {}
    _multiples = {}


class _Empty:
    pass

class _Multiple:
    def __init__(self, name, numMultiples, idOffset):
        self.name = name
        self.numMultiples = numMultiples
        self.identifiers = [str(i + idOffset) for i in range(numMultiples)]
        self.members = []
