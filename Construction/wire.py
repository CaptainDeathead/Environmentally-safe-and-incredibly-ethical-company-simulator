from typing import Dict, Tuple, List
from data import CHUNK_SIZE

class Wire:
    def __init__(self, location: Tuple, child):
        self.location: Tuple = location
        self.child: Wire = child

    def add_wire(self, child_wire):
        if self.child is None:
            self.child = child_wire
        else:
            current_child = self.child
            while current_child.child is not None:
                current_child = current_child.child
            current_child.child = child_wire