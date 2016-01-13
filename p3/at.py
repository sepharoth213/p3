
class IntegerAddress:
    def __init__(self,name,address,mask,shift):
        self.name = name
        self.address = address
        self.mask = mask
        self.shift = shift

    def get_value(self,value):
        return (int.from_bytes(value,byteorder='big') & self.mask) >> self.shift
