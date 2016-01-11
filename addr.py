
def toStr(addr):
    return hex(addr)[2:].upper()

def offsetAddr(addr,off):
    return toStr(int(addr,16) + off)

names = {}

'''

Defines some addresses in their hex form, and generates a names
dictionary from which to convert the string form of the address
to the correct name, to be able to print out what events are
being receieved

'''

playerOnePercent = "804530E0"
playerTwoPercent = "80453F70"
names[playerOnePercent] = "playerOnePercent"
names[playerTwoPercent] = "playerTwoPercent"

globalFrameCounter = "804D7420"
names[globalFrameCounter] = "globalFrameCounter"

controller1DigitalData = "804C1FAC"
controller1DigitalDataPrevious = "804C1FB0"
controller1ShoulderData = "804C1FC8"
controller1AnalogDataA = "804C1FC4"
controller1AnalogDataB = "804C1FCC"
names[controller1DigitalData] = "controller1DigitalData"
names[controller1DigitalDataPrevious] = "controller1DigitalDataPrevious"
names[controller1ShoulderData] = "controller1ShoulderData"
names[controller1AnalogDataA] = "controller1AnalogDataA"
names[controller1AnalogDataB] = "controller1AnalogDataB"

controllerOffset = 0x44

controller2DigitalData = offsetAddr(controller1DigitalData,controllerOffset)
controller2DigitalDataPrevious = offsetAddr(controller1DigitalDataPrevious,controllerOffset)
controller2ShoulderData = offsetAddr(controller1ShoulderData,controllerOffset)
controller2AnalogDataA = offsetAddr(controller1AnalogDataA,controllerOffset)
controller2AnalogDataB = offsetAddr(controller1AnalogDataB,controllerOffset)
names[controller2DigitalData] = "controller2DigitalData"
names[controller2DigitalDataPrevious] = "controller2DigitalDataPrevious"
names[controller2ShoulderData] = "controller2ShoulderData"
names[controller2AnalogDataA] = "controller2AnalogDataA"
names[controller2AnalogDataB] = "controller2AnalogDataB"

controller3DigitalData = offsetAddr(controller1DigitalData,controllerOffset*2)
controller3DigitalDataPrevious = offsetAddr(controller1DigitalDataPrevious,controllerOffset*2)
controller3ShoulderData = offsetAddr(controller1ShoulderData,controllerOffset*2)
controller3AnalogDataA = offsetAddr(controller1AnalogDataA,controllerOffset*2)
controller3AnalogDataB = offsetAddr(controller1AnalogDataB,controllerOffset*2)
names[controller3DigitalData] = "controller3DigitalData"
names[controller3DigitalDataPrevious] = "controller3DigitalDataPrevious"
names[controller3ShoulderData] = "controller3ShoulderData"
names[controller3AnalogDataA] = "controller3AnalogDataA"
names[controller3AnalogDataB] = "controller3AnalogDataB"

controller4DigitalData = offsetAddr(controller1DigitalData,controllerOffset*3)
controller4DigitalDataPrevious = offsetAddr(controller1DigitalDataPrevious,controllerOffset*3)
controller4ShoulderData = offsetAddr(controller1ShoulderData,controllerOffset*3)
controller4AnalogDataA = offsetAddr(controller1AnalogDataA,controllerOffset*3)
controller4AnalogDataB = offsetAddr(controller1AnalogDataB,controllerOffset*3)
names[controller4DigitalData] = "controller4DigitalData"
names[controller4DigitalDataPrevious] = "controller4DigitalDataPrevious"
names[controller4ShoulderData] = "controller4ShoulderData"
names[controller4AnalogDataA] = "controller4AnalogDataA"
names[controller4AnalogDataB] = "controller4AnalogDataB"

0x804530E0


locationsTxt = ""
for address in names:
    locationsTxt += address + "\n"

print(locationsTxt)
