from typing import List, Tuple
from data import *
from Chunks.chunk import Chunk
from utils import unique_number_from_pair

class ChunkManager:
    def __init__(self):
        self.position: Tuple = (0, 0)
        self.chunks: List = self.load_chunks(self.position)

    # Populate the chunks variable by creating new chunks based of the position and seed
    def load_chunks(self, position: Tuple):
        chunks: List = []
        for y in range(-1, 2):
            chunks.append([])
            for x in range(-1, 2):
                if abs(x) == 1 and abs(y) == 1: continue
                chunks[y].append(Chunk(position, unique_number_from_pair(x+self.position[0], y+position[1])))