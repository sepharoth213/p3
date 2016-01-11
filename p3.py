#!/usr/bin/env python3

import mw
import pad
import addr
import controller
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: ' + sys.argv[0] + ' dolphin-home')
    home = sys.argv[1]

    pad = pad.Pad(home + '/Pipes/p3')
    mw = mw.MemoryWatcher(home + '/MemoryWatcher/MemoryWatcher')

    currentFrame = 0;
    controller1 = controller.Controller();

    for address, value in mw:

        # update global frame count
        if address == addr.globalFrameCounter:
            currentFrame = int.from_bytes(value, byteorder='big')

        # track controller 1 digital inputs
        elif address == addr.controller1DigitalData:
            for button, press in controller1.updateDigitalData(value):
                print('frame ', currentFrame, ': ', button, ' pressed' if press else ' released')

        # print unhandled events
        elif address in addr.names:
            print('frame ', currentFrame, ': ', addr.names[address], value)