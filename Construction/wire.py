from typing import Dict, Tuple, List
from data import CHUNK_SIZE

class Wire:
    def __init__(self, path: Dict, from_structure, to_structure):
        self.path: Dict = path # { Chunk.location: [ (x, y), (x1, y1) ... ] }
        self.from_structure = from_structure
        self.to_structure = to_structure

    def draw(self, active_chunk_location: Tuple) -> List:
        ret_list: List = []

        for y in range(CHUNK_SIZE):
            ret_list.append([])
            for x in range(CHUNK_SIZE):
                ret_list[y].append(" ")

        if active_chunk_location in self.path:
            for coord in self.path[active_chunk_location]:
                ret_list[coord[1]][coord[0]] = "#"

        return ret_list