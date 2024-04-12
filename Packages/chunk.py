from typing import List, Tuple

class Chunk:
    def __init__(self, location: Tuple, chunk_id: int):
        self.location: Tuple = location
        self.chunk_id: int = chunk_id
        