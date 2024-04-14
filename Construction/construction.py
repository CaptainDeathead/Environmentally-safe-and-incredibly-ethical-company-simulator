from typing import List

class ConstructionManager:
    def __init__(self):
        self.wires: List = []
        self.chunk_connectors: List = []
        self.hubs: List = []
        self.extractors: List = []
        self.generators: List = []