from typing import List
from chunk_manager import ChunkManager
from data import *

class Game:
    def __init__(self):
        self.chunk_manager: ChunkManager = ChunkManager()
        self.