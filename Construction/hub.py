from typing import List

class Hub:
    def __init__(self, chunk_id):
        self.nodes: List = [[False,False,False] for _ in range(3)]

    def reset_nodes(self):
        self.nodes: List = [[False,False,False] for _ in range(3)]