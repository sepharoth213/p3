
def toStr(addr):
    return hex(addr)[2:].upper()

names = {}

'''

Defines some addresses in their hex form, and generates a names
dictionary from which to convert the string form of the address
to the correct name, to be able to print out what events are
being receieved

'''

playerOnePercent = 0x804530E0
names[toStr(playerOnePercent)] = "playerOnePercent"
playerTwoPercent = 0x80453F70
names[toStr(playerTwoPercent)] = "playerTwoPercent"
globalFrameCounter = 0x804D7420
names[toStr(globalFrameCounter)] = "globalFrameCounter"

controller1DigitalData = 0x804C1FAC
names[toStr(controller1DigitalData)] = "controller1DigitalData"
controller1DigitalDataPrevious = 0x804C1FB0
names[toStr(controller1DigitalDataPrevious)] = "controller1DigitalDataPrevious"
controller1ShoulderData = 0x804C1FC8
names[toStr(controller1ShoulderData)] = "controller1ShoulderData"
controller1AnalogDataA = 0x804C1FC4
names[toStr(controller1AnalogDataA)] = "controller1AnalogDataA"
controller1AnalogDataB = 0x804C1FCC
names[toStr(controller1AnalogDataB)] = "controller1AnalogDataB"

controllerOffset = 0x44
