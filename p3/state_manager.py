import struct

from p3.state import State
from p3.state import PlayerType
from p3.state import Character
from p3.state import Menu
from p3.state import Stage
from p3.state import ActionState

def add_address(x, y):
    """Returns a string representation of the sum of the two parameters.

    x is a hex string address that can be converted to an int.
    y is an int.
    """
    return "{0:08X}".format(int(x, 16) + y)

class StateManager:
    """Converts raw memory changes into attributes in a State object."""
    def __init__(self, state):
        """Pass in a State object. It will have its attributes zeroed."""
        self.state = state
        self.addresses = {}

        self.addresses['80479D60'] = self.int_handler(self.state, 'frame')
        self.addresses['80479D30'] = self.int_handler(self.state, 'menu', 0, 0xFF, Menu, Menu.Characters)
        self.addresses['804D6CAC'] = self.int_handler(self.state, 'stage', 8, 0xFF, Stage, Stage.Unselected)

        self.state.players = []
        for player_id in range(4):
            player = State()
            self.state.players.append(player)
            data_pointer = add_address('80453130', 0xE90 * player_id)

            type_address = add_address('803F0E08', 0x24 * player_id)
            type_handler = self.int_handler(player, 'type', 24, 0xFF, PlayerType, PlayerType.Unselected)
            character_handler = self.int_handler(player, 'character', 8, 0xFF, Character, Character.Unselected)
            self.addresses[type_address] = [type_handler, character_handler]

            state_address = data_pointer + ' 70'
            state_handler = self.int_handler(player, 'action_state', 0, 0xFFFF)#, ActionState, ActionState.Unselected)
            self.addresses[state_address] = state_handler
            
            x_address = data_pointer + ' 110'
            x_handler = self.float_handler(player, 'x')
            self.addresses[x_address] = x_handler

            y_address = data_pointer + ' 114'
            y_handler = self.float_handler(player, 'y')
            self.addresses[y_address] = y_handler

            ground_address = data_pointer + ' 140'
            ground_handler = self.int_handler(player, 'on_ground', 0, 0xFFFF, lambda x: x == 0, True)
            self.addresses[ground_address] = ground_handler

            facing_address = data_pointer + ' 8C'
            facing_handler = self.float_handler(player, 'facing')
            self.addresses[facing_address] = facing_handler

            vertical_velocity_address = data_pointer + ' E4'
            vertical_velocity_handler = self.float_handler(player, 'vertical_velocity')
            self.addresses[vertical_velocity_address] = vertical_velocity_handler

            horizontal_air_velocity_address = data_pointer + ' E0'
            horizontal_air_velocity_handler = self.float_handler(player, 'horizontal_air_velocity')
            self.addresses[horizontal_air_velocity_address] = horizontal_air_velocity_handler

            horizontal_ground_velocity_address = data_pointer + ' 14C'
            horizontal_ground_velocity_handler = self.float_handler(player, 'horizontal_ground_velocity')
            self.addresses[horizontal_ground_velocity_address] = horizontal_ground_velocity_handler

            fastfall_velocity_address = data_pointer + ' 1E4'
            fastfall_velocity_handler = self.float_handler(player, 'fastfall_velocity')
            self.addresses[fastfall_velocity_address] = fastfall_velocity_handler

            hitlag_counter_address = data_pointer + ' 19BC'
            hitlag_counter_handler = self.float_handler(player, 'hitlag_counter')
            self.addresses[hitlag_counter_address] = hitlag_counter_handler

            jumps_used_address = data_pointer + ' 19C8'
            jumps_used_handler = self.int_handler(player, 'jumps_used', 0, 0x000000FF)
            self.addresses[jumps_used_address] = jumps_used_handler

    def handle(self, address, value):
        """Convert the raw address and value into changes in the State."""
        assert address in self.addresses
        handlers = self.addresses[address]
        if isinstance(handlers, list):
            for handler in handlers:
                handler(value)
        else:
            handlers(value)

    def locations(self):
        """Returns a list of addresses for exporting to Locations.txt."""
        return self.addresses.keys()


    def int_handler(self, obj, name, shift=0, mask=0xFFFFFFFF, wrapper=None, default=0):
        """Returns a handler that sets an attribute for a given object.

        obj is the object that will have its attribute set. Probably a State.
        name is the attribute name to be set.
        shift will be applied before mask.
        Finally, wrapper will be called on the value if it is not None.

        This sets the attribute to default when called. Note that the actual final
        value doesn't need to be an int. The wrapper can convert int to whatever.
        This is particularly useful for enums.
        """
        def handle(value):
            transformed = (struct.unpack('>i', value)[0] >> shift) & mask
            wrapped = transformed if wrapper is None else wrapper(transformed)
            setattr(obj, name, wrapped)
            for cb in getattr(obj, name + "_changed"):
                cb(self.state)
        setattr(obj, name, default)
        setattr(obj, name + "_changed", [])
        return handle

    def float_handler(self, obj, name, wrapper=None, default=0.0):
        """Returns a handler that sets an attribute for a given object.

        Similar to int_handler, but no mask or shift.
        """
        def handle(value):
            as_float = struct.unpack('>f', value)[0]
            setattr(obj, name, as_float if wrapper is None else wrapper(as_float))
            for cb in getattr(obj, name + "_changed"):
                cb(self.state)
        setattr(obj, name, default)
        setattr(obj, name + "_changed", [])
        return handle
