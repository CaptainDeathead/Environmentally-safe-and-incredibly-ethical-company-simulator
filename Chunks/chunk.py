from typing import List, Tuple
from utils import unique_number_from_pair
from data import *
from random import seed, choices

class Chunk:
    def __init__(self, location: Tuple, chunk_id: int):
        self.location: Tuple = location
        self.chunk_id: int = chunk_id
        self.chunk_seed: int = unique_number_from_pair(chunk_id, SEED)
        self.chunk_map: List = []
        self.generate()

    # Populates chunk_map with resource deposits and empty space
    def generate(self):
        for y in range(CHUNK_SIZE):
            self.chunk_map.append([])
            for x in range(CHUNK_SIZE):
                self.chunk_map[y].append(self.get_cell_type((x+1)*(y+1)+self.chunk_seed))
                
    # Takes in a large integer and checks if any deposits are spawned and returns a string corresponding to the deposit
    def get_cell_type(self, cell_num: int) -> str:
        seed(cell_num)

        total_chance = sum(DEPOSIT_SPAWN_CHANCES.values())
        probabilities = {DEPOSIT_SPAWN_CHANCES[deposit_type] / total_chance for deposit_type in DEPOSIT_TYPES}

        deposit = choices(DEPOSIT_TYPES, weights=probabilities)[0]
        
        return SYMBOLS[deposit]