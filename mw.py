import binascii
import os
import socket

class MemoryWatcher:
    """Reads and parses game memory changes."""
    def __init__(self, path):
        """Creates the socket if it does not exist, and then opens it."""
        try:
            os.unlink(path)
        except OSError:
            pass
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self.sock.bind(path)

    def __iter__(self):
        """Iterate over this class in the usual way to get memory changes."""
        return self

    def __del__(self):
        """Closes the socket."""
        self.sock.close()

    def __next__(self):
        """Blocks until it has read a pair: (address, value).
        
        address is the string provided by dolphin, set in Locations.txt.
        value is a raw byte string, suitable for interpretation with struct.
        
        """
        try:
            data = self.sock.recvfrom(1024)[0].decode('utf-8').splitlines()
        except OSError:
            raise StopIteration
        assert len(data) == 2
        # Strip the null terminator, pad with zeros, then convert to bytes
        return data[0].upper(), binascii.unhexlify(data[1].strip('\x00').zfill(8))
        # return data[0].upper(), binascii.unhexlify(data[1].strip('\x00').zfill(8))
