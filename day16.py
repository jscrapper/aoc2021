from aoc2021 import Day
from io import StringIO
import numpy as np
class Packet():
    def __init__(self, stream:StringIO):
        self.stream = stream
        self.start = stream.tell()
        self.version = int(stream.read(3), 2)
        self.typeid = int(stream.read(3), 2)
        self.value = 0
        self.subpackets = []
        if self.typeid == 4:
            binstring = ""
            while True:
                end = stream.read(1) == "0"
                binstring += stream.read(4)
                if end: 
                    break
            self.value = int(binstring,2)
        else:
            self.length_typeid = stream.read(1)
            if self.length_typeid == "0":   # length is a 15-bit number representing the number of bits in the sub-packets
                num_bits = int(stream.read(15), 2)
                start = stream.tell()
                end = start + num_bits
                while stream.tell() < end:
                    self.subpackets.append(Packet(self.stream))
            else:   # the length is a 11-bit number representing the number of sub-packets.
                num_elems = int(stream.read(11), 2)
                for i in range(num_elems):
                    self.subpackets.append(Packet(self.stream))

        if self.typeid == 0: # sum
            self.value = sum([p.value for p in self.subpackets])
        elif self.typeid == 1: # product
            self.value = np.product([p.value for p in self.subpackets])
        elif self.typeid == 2: # min
            self.value = np.min([p.value for p in self.subpackets])
        elif self.typeid == 3: # max
            self.value = np.max([p.value for p in self.subpackets])
        elif self.typeid == 5: # gt
            self.value =  int(self.subpackets[0].value > self.subpackets[1].value)
        elif self.typeid == 6: # lt
            self.value =  int(self.subpackets[0].value < self.subpackets[1].value)
        elif self.typeid == 7: # eq
            self.value =  int(self.subpackets[0].value == self.subpackets[1].value)

    def versions(self):
        vers=[self.version]
        for p in self.subpackets:
            vers.extend(p.versions())
        return vers
    
    def count_versions(self):
        return sum(self.versions())

    @classmethod
    def from_hex(cls, hexstr):
        bitsize=len(hexstr)*4
        data = f'{int(hexstr,16):0>{bitsize}b}' #format here removes '0b' from the front, and > formats as big endian
        stream = StringIO(data)
        return cls(stream)

class Day16(Day):

    def get_test_input(self):
        return ["9C0141080250320F1802104A08"]
    
    def parse_input(self):
        return [Packet.from_hex(x) for x in self.raw_puzzle_input]

    def a(self):
        return self.puzzle_input[0].count_versions()

    def b(self):
        return self.puzzle_input[0].value

if __name__ == "__main__": 
    Day16(False).run()