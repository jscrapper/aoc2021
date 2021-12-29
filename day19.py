from numpy.core.fromnumeric import shape
from aoc2021 import Day
import os
from scipy.spatial import KDTree, distance
from scipy.spatial.transform import Rotation as R
import numpy as np
from itertools import product

class Day19(Day):

    def _input(self, filename):
        with open(filename, 'r') as f:
            raw_puzzle_input = f.read()
        return raw_puzzle_input

    def get_input(self):
        filename = os.path.join(os.path.dirname(__file__), self.__class__.__name__+".txt")
        return self._input(filename)

    def get_test_input(self):
        filename = os.path.join(os.path.dirname(__file__), self.__class__.__name__+"_test.txt")
        return self._input(filename)
    
    def parse_input(self):
        scanners=[] # list of scanners

        for group in self.raw_puzzle_input.strip().split('\n\n'):
            scanners.append([tuple(map(int, beacon.split(','))) for beacon in group.split('\n')[1:]])

        beacons = set(scanners.pop(0))
        scanner_positions = []

        def find_match(beacon_tree, _scanners):
            for scanner in _scanners:
                tree=KDTree(scanner)
                for scanner_beacon in scanner:
                    scanner_neighbors=tree.query(scanner_beacon, k=3)
                    d=sum(scanner_neighbors[0])
                    for beacon in beacons:
                        beacon_neighbors = beacon_tree.query(beacon, k=3)
                        if sum(beacon_neighbors[0]) == d:
                            return scanner, [beacon_tree.data[i] for i in beacon_neighbors[1]], [tree.data[i] for i in scanner_neighbors[1]]
            return None, None, None

        def find_rotation(bn, sn):
            beacon_offset=(bn[0]-bn[1]).round().astype(np.int32)
            for r in ROTATIONS:
                rotated=r.apply(sn)
                scanner_offset=(rotated[0]-rotated[1]).round().astype(np.int32)
                if all(scanner_offset==beacon_offset):
                    return r, (bn[0]-rotated[0]).round().astype(np.int32)

        while len(scanners) > 0:

            beacon_tree = KDTree(list(beacons))
            
            # find a scanner that shares at least 3 beacons
            scanner, beacon_neighbors, scanner_neighbors = find_match(beacon_tree, scanners)
            scanners.remove(scanner)
            
            # find orientation of matching scanner
            rot, offset = find_rotation(beacon_neighbors, scanner_neighbors)
            oriented_scanner = rot.apply(scanner).round().astype(np.int32)
            translated_scanner = oriented_scanner + offset

            scanner_positions.append(offset)

            # update the beacons set with unique beacons. 
            beacons.update([tuple(map(int,x)) for x in translated_scanner])

        return beacons, scanner_positions


    def a(self):
        return len(self.puzzle_input[0])

    def b(self):
        return int(max(distance.pdist(self.puzzle_input[1], metric="cityblock")))

def get_rotations():
    rotations=[]
    for p in product([0,90,180,270],repeat=3):
        rot=R.from_euler('zyx', p, degrees=True)
        unique=True
        for existing in rotations:
            if (rot.as_matrix().round()==existing.as_matrix().round()).all():
                unique = False
        if unique:
            rotations.append(rot)
    return rotations
ROTATIONS=get_rotations()

if __name__ == "__main__":
    Day19().run()
    # get_rotations()