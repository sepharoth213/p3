import struct

class IntegerAddress:
    def __init__(self,name,address,shift = 0, mask = 0xFFFFFFFF):
        self.name = name
        self.address = address
        self.mask = mask
        self.shift = shift

    def get_value(self,value):
        return (int.from_bytes(value,byteorder='big') >> self.shift) & self.mask 

class FloatAddress:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def get_value(self,value):
        return struct.unpack('f', value)[0]

class BooleanAddress:
    def __init__(self,name,address,compareValue,shift = 0, mask = 0xFFFFFFFF):
        self.name = name
        self.address = address
        self.mask = mask
        self.shift = shift
        self.compareValue = compareValue

    def get_value(self,value):
        return ((int.from_bytes(value,byteorder='big') >> self.shift) & self.mask == int(self.compareValue, 16))
