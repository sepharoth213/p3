import enum

def toStr(addr):
    return hex(addr)[2:].upper()

def offsetAddr(addr,off):
    return toStr(int(addr,16) + off)

names = {}

'''

Defines some addresses, and generates a names dictionary

'''

controllerOffset = 0x44

class Addresses(enum.Enum):
    playerOnePercent = "804530E0"
    playerTwoPercent = "80453F70"

    globalFrameCounter = "804D7420"

    controller1DigitalData = "804C1FAC"
    controller1DigitalDataPrevious = "804C1FB0"
    controller1ShoulderData = "804C1FC8"
    controller1AnalogDataA = "804C1FC4"
    controller1AnalogDataB = "804C1FCC"

    controller2DigitalData = offsetAddr(controller1DigitalData,controllerOffset)
    controller2DigitalDataPrevious = offsetAddr(controller1DigitalDataPrevious,controllerOffset)
    controller2ShoulderData = offsetAddr(controller1ShoulderData,controllerOffset)
    controller2AnalogDataA = offsetAddr(controller1AnalogDataA,controllerOffset)
    controller2AnalogDataB = offsetAddr(controller1AnalogDataB,controllerOffset)

    controller3DigitalData = offsetAddr(controller1DigitalData,controllerOffset*2)
    controller3DigitalDataPrevious = offsetAddr(controller1DigitalDataPrevious,controllerOffset*2)
    controller3ShoulderData = offsetAddr(controller1ShoulderData,controllerOffset*2)
    controller3AnalogDataA = offsetAddr(controller1AnalogDataA,controllerOffset*2)
    controller3AnalogDataB = offsetAddr(controller1AnalogDataB,controllerOffset*2)

    controller4DigitalData = offsetAddr(controller1DigitalData,controllerOffset*3)
    controller4DigitalDataPrevious = offsetAddr(controller1DigitalDataPrevious,controllerOffset*3)
    controller4ShoulderData = offsetAddr(controller1ShoulderData,controllerOffset*3)
    controller4AnalogDataA = offsetAddr(controller1AnalogDataA,controllerOffset*3)
    controller4AnalogDataB = offsetAddr(controller1AnalogDataB,controllerOffset*3)

locationsTxt = ""
for address in Addresses:
    locationsTxt += address.value + "\n"
    names[address.value] = address