from typing import List, Tuple
from data import *
from Packages.chunk import Chunk

def unique_number_from_pair(a, b):
    return hash(str(a) + ',' + str(b))

class ChunkManager:
    def __init__(self):
        self.position: Tuple = (0, 0)
        self.chunks: List = self.load_chunks(self.position)

    def load_chunks(self, load_all, position: Tuple):
        chunks: List = []
        for y in range(-1, 2):
            chunks.append([])
            for x in range(-1, 2):
                chunks[y].append(Chunk())