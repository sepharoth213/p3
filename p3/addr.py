import enum
import itertools

from p3 import at

class AddressObjects:
    """Holds data for turning addresses into data."""

    @classmethod
    def init(cls):
        """Generates AddressObjects and data for add_multiples_accessors."""
        cls.address_objects = [
            
            at.IntegerAddress("stageID", "804D6CAD", 16),
            at.IntegerAddress("frameCount", "8046B6CC", 16),
            at.IntegerAddress("currentMenu", "8065CC14", 20, 0xF),

            at.IntegerAddress("globalPowerOnCounter", "804D7420"),
            at.IntegerAddress("globalFrameCounter", "80479D60"),
        ]

        cls._add_multiple("player", 4, 1)
        cls._add_multiple("controller", 4, 1)

        cls._multiple_address("player", "Percent",     at.IntegerAddress, "804530E0",      "E90", (16))
        cls._multiple_address("player", "Stocks",      at.IntegerAddress, "8045310E",      "E90", (24))
        cls._multiple_address("player", "Character",   at.IntegerAddress, "803F0E08",      "14",  (0, 0xFF))
        cls._multiple_address("player", "ActionState", at.IntegerAddress, "80453130 70",   "E90")
        cls._multiple_address("player", "JumpsUsed",   at.IntegerAddress, "80453130 19C8", "E90", (24))

        cls._multiple_address("player", "InAir", at.BooleanAddress, "80453130 140", "E90", ("1"))

        cls._multiple_address("player", "X",              at.FloatAddress, "80453090",      "E90")
        cls._multiple_address("player", "Y",              at.FloatAddress, "80453094",      "E90")
        cls._multiple_address("player", "AnimationSpeed", at.FloatAddress, "80453130 8FC",  "E90")
        cls._multiple_address("player", "Facing",         at.FloatAddress, "80453130 8C",   "E90")
        cls._multiple_address("player", "DeltaY",         at.FloatAddress, "80453130 12C",  "E90")
        cls._multiple_address("player", "HitlagFrames",   at.FloatAddress, "80453130 19BC", "E90")
        cls._multiple_address("player", "ShieldSize",     at.FloatAddress, "80453130 19F8", "E90")
        cls._multiple_address("player", "HitstunFrames",  at.FloatAddress, "80453130 23A0", "E90")

        locations_txt = ""
        for address in cls.address_objects:
            locations_txt += address.address + "\n"
            cls._address_map[address.address] = address
            cls._name_map[address.name] = address

        cls.add_multiples_accessors(cls._name_map)

    @classmethod
    def get_by_address(cls,address):
        """Returns an address object with the given address.
        Use this to parse MemoryWatcher output."""
        return cls._address_map[address]

    @classmethod
    def get_by_name(cls,name):
        """Returns an address object with the given name."""
        return cls._name_map[name]

    @classmethod
    def add_multiples_accessors(cls,addressDict):
        """Adds iterable accessors to a game state map.
        Indices always begin at 0 regardless of identifier offset.

        For example:
        addressDict["player"][1].Stocks()
        will evaluate to:
        addressDict["player2Stocks"]

        """
        for key, multiple in cls._multiples.items():
            addressDict[multiple.name] = []
            instance = {}
            for i in range(multiple.numMultiples):
                multipleObj = _Empty()
                for member in multiple.members:
                    # lambdas are nested so they can capture the value
                    # of their respective variables during the loop
                    setattr(multipleObj, member,
                        (lambda a: \
                            (lambda b: \
                                (lambda c:\
                                    lambda: addressDict[a.name + str(a.identifiers[b]) + c]\
                                )(member)
                            )(i)
                        )(multiple)
                    )
                addressDict[multiple.name].append(multipleObj)

    _address_map = {}
    _name_map = {}
    _multiples = {}

    @classmethod
    def _add_multiple(cls,name,numMultiples,nameOffset):
        """creates a _Multiple object for the _multiple_address function."""
        cls._multiples[name] = _Multiple(name,numMultiples,nameOffset)

    @classmethod
    def _multiple_address(cls,multipleName,field,addressType,address,addressOffset,args = ()):
        """Creates multiple adjacent addresseses.

        multipleName must be one added by _add_multiple().
        field is the name that will be appended to the end of the address name.
        addressType is a class from at.py.
        address is the address of the first address object.
        addressOffset is the "distance" between addresses.
        args is a tuple or single value that will be appended to the address name
            and expanded as the argument to the addressType constructor.

        addressOffset will be intelligently added to the address:
        an address of "FF00 FF00 FF00" plus an offset of "1 2 3" will
        result in an address "FF01 FF02 FF03"

        """
        assert(multipleName in cls._multiples)
        multiple = cls._multiples[multipleName]
        multiple.members.append(field)
            
        baseAddress = [i for i in map(lambda o: int(o, 16), address.split())]
        offsets = [i for i in map(lambda o: int(o, 16), addressOffset.split())]

        #force args to be a tuple if it is not one
        if not isinstance(args, tuple):
            args = (args,)

        #ensure offset isn't incrementing nonexistent address data
        assert(len(baseAddress) >= len(offsets))

        for i in range(multiple.numMultiples):
            name = multipleName + str(multiple.identifiers[i]) + field
            address = ""

            #generate address
            for b, o in itertools.zip_longest(baseAddress,offsets):
                if o is not None:
                    address += hex(b + o*i)[2:] + " "
                else:
                    address += hex(b)[2:] + " "

            #remove trailing space
            address = str.upper(address[:-1])

            newArgs = tuple([name,address] + list(args))
            cls.address_objects.append(addressType(*newArgs))


#needed for add_multiple_accessors
class _Empty:
    pass

class _Multiple:
    def __init__(self, name, numMultiples, idOffset):
        """Holds data for multiples and generates the identifiers based on the idOffset""" 
        self.name = name
        self.numMultiples = numMultiples
        self.identifiers = [i + idOffset for i in range(numMultiples)]
        self.members = []