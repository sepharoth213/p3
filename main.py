
import sys, os, json
from p3.melee import Melee
from p3.addr import AddressObjects

inGame = False;
toSave = [];
saveNum = 0;

def listener (name, value):
    global inGame
    toSave.append([name,value])
    if name[:4] == "cont":
        print(name,value)
    # if inGame:
        # print(ao.name, " ", value)

def menuCallback(event, gameState):
    global inGame, toSave, saveNum
    # print("menu " + str(event.value))
    if event.value == 13 and inGame == False:
        inGame = True;
        toSave = []
        print('starting record')
    elif event.value != 13 and inGame == True:
        inGame = False
        pathName = sys.argv[2] + str(saveNum) + ".json"
        while(os.path.exists(pathName)):
            saveNum += 1
            pathName = sys.argv[2] + str(saveNum) + ".json"
        # pickle.dump( toSave, open( pathName, "wb" ) )
        # with open(pathName, 'w') as outfile:
        #     json.dump(toSave, outfile)
        saveNum += 1
        print('ended record ' + pathName)

if __name__ == '__main__':
    AddressObjects.init()
    print(AddressObjects.locations_txt)
    if len(sys.argv) != 3:
        sys.exit('Usage: ' + sys.argv[0] + ' dolphin-home savepath')
    home = sys.argv[1]

    melee = Melee()

    melee.add_listener("currentMenu",menuCallback)
    melee.listen(home,listener)