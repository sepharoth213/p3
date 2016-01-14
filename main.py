
import sys
from p3.melee import Melee

def listener (event, gameState):
    print(event.name, " ", gameState)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: ' + sys.argv[0] + ' dolphin-home')
    home = sys.argv[1]

    melee = Melee()

    # melee.add_listener("globalFrameCounter",listener)
    melee.listen(home,listener)