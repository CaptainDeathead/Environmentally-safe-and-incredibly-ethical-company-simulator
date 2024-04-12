from typing import List, Tuple
from utils import unique_number_from_pair
from data import *

class Chunk:
    def __init__(self, location: Tuple, chunk_id: int):
        self.location: Tuple = location
        self.chunk_id: int = chunk_id
        self.chunk_seed: int = unique_number_from_pair(chunk_id, SEED)
        self.chunk_map: List

    # Populates chunk_map with resource deposits and empty space
    def generate(self):
        for y in range(CHUNK_SIZE):
            self.chunk_map.append([])
            for x in range(CHUNK_SIZE):
                self.chunk_map[y].append(self.get_cell_type(x*y*self.chunk_seed))
                
    # Takes in a large integer and checks if any deposits are spawned and returns a string corresponding to the deposit
    def get_cell_type(self, cell_num: int) -> str:
        cell_char: str = ' '
        for deposit_type in DEPOSIT_TYPES:
            if cell_num % DEPOSIT_SPAWN_CHANCES[deposit_type] == 0: cell_char = SYMBOLS[deposit_type]
        
        return cell_char