from base64 import b64encode
from io import BytesIO
from .stream import BinStream

class RST:
    __slots__ = ('entries', 'version', 'hash_bits', 'has_trenc', 'count')

    def __init__(self, entries = dict(), version = 5, hash_bits = 38, has_trenc=False, count = 0):
        self.entries = entries
        self.version = version
        # We assume we are in latest uwu
        self.hash_bits = hash_bits
        self.has_trenc = has_trenc
        self.count = count

    def __json__(self):
        return {key: getattr(self, key) for key in self.__slots__}

    def stream(self, path, mode, raw=None):
        if raw != None:
            if raw == True:  # the bool True value
                return BinStream(BytesIO())
            else:
                return BinStream(BytesIO(raw))
        return BinStream(open(path, mode))

    def read(self, path, raw=None):
        # Credits https://github.com/CommunityDragon/CDTB/blob/master/cdtb/rstfile.py
        with self.stream(path, 'rb', raw) as f:
            magic, = f.read_s(3)
            self.version, = f.read_u8()
            if magic != "RST":
                raise Exception(f'pyRitoFile: invalid magic for RST file "{magic}"')
            
            if self.version != 5:
                raise Exception(f'pyRitoFile: unsupported RST version "{self.version}"')
            

            hash_mask = (1 << self.hash_bits) - 1
            self.count, = f.read_ul()
            entries = []

            # what is this bro ;-;
            for _ in range(self.count):
                v, = f.read_ull()
                entries.append((v >> self.hash_bits, v & hash_mask))
            
            data = f.stream.read()
            for i, h in entries:
                end = data.find(b"\0", i)
                d = data[i:end]
                self.entries[h] = (d.decode('utf-8', 'replace'), v)
            
            
    def write(self, path, raw=None):
        raise RuntimeError("pyritofile: RST Writing not supported")