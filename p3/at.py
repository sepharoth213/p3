import struct

class AddressObject:
    def __init__(self,address):
        self.address = address
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def parse_bytes(self,value):
        for obj in self.objects:
            yield (obj.name, obj.parse_bytes(value))

class IntegerAddress:
    def __init__(self,name,address,shift = 0, mask = 0xFFFFFFFF):
        self.name = name
        self.address = address
        self.mask = mask
        self.shift = shift

    def parse_bytes(self,value):
        return (int.from_bytes(value,byteorder='big') >> self.shift) & self.mask 

class FloatAddress:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def parse_bytes(self,value):
        return struct.unpack('>f', value)[0]

class BooleanAddress:
    def __init__(self,name,address,compare_value,shift = 0, mask = 0xFFFFFFFF):
        self.name = name
        self.address = address
        self.mask = mask
        self.shift = shift
        self.compare_value = compare_value
        
    def parse_bytes(self,value):
        return ((int.from_bytes(value,byteorder='big') >> self.shift) & self.mask == int(self.compare_value, 16))
