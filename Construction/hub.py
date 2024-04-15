from typing import List

class Hub:
    def __init__(self, chunk_id):
        self.nodes: List = [[None,None,None] for _ in range(3)]