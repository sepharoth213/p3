from . import mw, pad, at, addr
from collections import OrderedDict

class Event:
    def __init__(self, value):
        self.__name = None
        self.value = value

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Melee:
    def __init__(self):
        self._listeners = {}
        self.gameState = {}

    def listen(self,home,callback):

        watcher = mw.MemoryWatcher(home + '/MemoryWatcher/MemoryWatcher')
        for address, value in watcher:
            ao = addr.AddressObjects.get_by_address(address)
            
            parsedValue = ao.parse_bytes(value)
            self.gameState[ao.name] = parsedValue
            
            callback(ao,parsedValue)
            self.dispatch(ao.name, Event(parsedValue))

    def dispatch(self, eventName, event=None):
        if event is None:
            event = Event()
        elif not isinstance(event, Event):
            raise ValueError('Unexpected event type given')
        event.setName(eventName)
        if eventName not in self._listeners:
            return event
        for listener in self._listeners[eventName].values():
            listener(event, self.gameState)
        return event

    def add_listener(self, eventName, listener, priority=0):
        if eventName not in self._listeners:
            self._listeners[eventName] = {}
        self._listeners[eventName][priority] = listener
        self._listeners[eventName] = OrderedDict(sorted(self._listeners[eventName].items(), key=lambda item: item[0]))

    def remove_listener(self, eventName, listener=None):
        if eventName not in self._listeners:
            return
        if not listener:
            del self._listeners[eventName]
        else:
            for p, l in self._listeners[eventName].items():
                if l is listener:
                    self._follisteners[eventName].pop(p)
                    return