
class IntegerAddress:
    def __init__(self,name,address,shift, mask = 0xFFFFFFFF):
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
        self.mask = mask
        self.shift = shift

    def get_value(self,value):
        # return (int.from_bytes(value,byteorder='big') >> self.shift) & self.mask 
        return 0
