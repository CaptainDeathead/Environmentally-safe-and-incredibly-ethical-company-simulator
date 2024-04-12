from typing import List
from Chunks.chunk_manager import ChunkManager
from data import *
from utils import *
from user_input import get_input
from table import table_from_2d_list

class Game:
    def __init__(self):
        self.chunk_manager: ChunkManager = ChunkManager()
        
    def main(self):
        while 1:
            cls()
            print(table_from_2d_list(self.chunk_manager.chunks[1][1].chunk_map))
            get_input()