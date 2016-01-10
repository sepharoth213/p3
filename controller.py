
class Button:
    def __init__(self,name,offset):
        self.name = name
        self.offset = offset
        self.press = False;

class Controller:

    def __init__(self):
        self.buttons = [
                Button("buttonS",12),
                Button("buttonY",11),
                Button("buttonX",10),
                Button("buttonB",9),
                Button("buttonA",8),
                Button("buttonR",6),
                Button("buttonL",5),
                Button("buttonZ",4),
                Button("dpadU",3),
                Button("dpadD",2),
                Button("dpadR",1),
                Button("dpadL",0)
            ]

    # generator that returns tuples for each button that
    # changed state in the form (button name, buttonpressed)
    def updateDigitalData(self,valueBytes):
        for button in self.buttons:
            press = ((int.from_bytes(valueBytes,byteorder='big') >> button.offset) & 1) == 1
            if press != button.press:
                if press:
                    yield ((button.name,True))
                else:
                    yield ((button.name,False))
                button.press = press