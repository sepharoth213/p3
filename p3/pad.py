import enum
import os

@enum.unique
class Button(enum.Enum):
    A = 0
    B = 1
    X = 2
    Y = 3
    Z = 4
    START = 5
    L = 6
    R = 7
    D_UP = 8
    D_DOWN = 9
    D_LEFT = 10
    D_RIGHT = 11

@enum.unique
class Trigger(enum.Enum):
    L = 0
    R = 1

@enum.unique
class Stick(enum.Enum):
    MAIN = 0
    C = 1

class Pad:
    """Writes out controller inputs."""
    def __init__(self, path):
        """Opens the fifo. Blocks until the other end is listening."""
        try:
            os.mkfifo(path)
        except OSError:
            pass
        self.pipe = open(path, 'w', buffering=1)

    def __del__(self):
        """Closes the fifo."""
        self.pipe.close()

    def press_button(self, button):
        """Press a button."""
        assert button in Button
        self.pipe.write('PRESS {}\n'.format(button.name))

    def release_button(self, button):
        """Release a button."""
        assert button in Button
        self.pipe.write('RELEASE {}\n'.format(button.name))

    def press_trigger(self, trigger, amount):
        """Press a trigger. Amount is in [0, 1], with 0 as released."""
        assert trigger in Trigger
        assert 0 <= amount <= 1
        self.pipe.write('SET {} {:.2f}\n'.format(trigger.name, amount))

    def tilt_stick(self, stick, x, y):
        """Tilt a stick. x and y are in [0, 1], with 0.5 as neutral."""
        assert stick in Stick
        assert 0 <= x <= 1 and 0 <= y <= 1
        self.pipe.write('SET {} {:.2f} {:.2f}\n'.format(stick.name, x, y))
