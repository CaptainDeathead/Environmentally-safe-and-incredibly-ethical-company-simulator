from typing import Dict, List
from Construction.wire import Wire
from data import CHUNK_SIZE

class ConstructionManager:
    def __init__(self):
        self.wires: Dict = {}
        self.chunk_connectors: List = []
        self.hubs: List = []
        self.extractors: List = []
        self.generators: List = []

    def build(self, item, chunk_id: int = None):
        if item == 'wire': self.place_wire(chunk_id)

    def place_wire(self, chunk_id: int):
        points: List = []
        
        print("Building: wire\n")
        
        point_type: str = "first"

        while 1:
            new_point: str = input(f"Enter the {point_type} point in ('x,y' | e.g. '1,3') format between 1 and {CHUNK_SIZE} ('c' to end wire): ")

            if new_point == 'c': break

            if ',' not in new_point:
                print("Incorrect format! Make sure you have a comma.")
                continue
            
            new_point_x, new_point_y = new_point.split(',')
            new_point_x = new_point_x.replace(' ', '')
            new_point_y = new_point_y.replace(' ', '')

            if not (new_point_x.isdigit() and new_point_y.isdigit()):
                print("Please make sure your coordinates are valid whole numbers!")
                continue

            new_point_x = int(new_point_x)-1
            new_point_y = int(new_point_y)-1

            if point_type == "next":
                if points[-1] == (new_point_x, new_point_y):
                    print("You just entered that point, try a different one!")
                    continue

                filling_x: bool = new_point_y == points[-1][1]
                if filling_x and new_point_x == points[-1][0]:
                    print("Please ensure you enter the coordinates on either the x or y axis but not both so that the wires are in streight lines!\ne.g. The previous point was '2,2' then the next point has to be something like: '5,2' or '2,1' not '3, 6' because it would be diagonal.")
                    continue
                elif filling_x:
                    for x in range(points[-1][0], new_point_x):
                        points.append((x, new_point_y))
                else:
                    for y in range(points[-1][1], new_point_y):
                        points.append((new_point_x, y))
            
            points.append((new_point_x, new_point_y))

            point_type = "next"

        # add the chunk to the wires dict
        if chunk_id not in self.wires:
            self.wires[chunk_id] = []

        if len(points) == 0: return
        
        if len(points) == 1:
            self.wires[chunk_id].append(Wire(points[0], None))
            return
        
        if len(points) == 2:
            self.wires[chunk_id].append(Wire(points[0], Wire(points[1], None)))
            return
        
        new_wire = Wire(points[0], None)

        # new wire will contain a reference to current_wire (they reference the same object)
        # basicly new_wire is a reference to the initial wire created, and has current_wire keeps walking further and further, new_wire still contains the reference to the starting wire, which is also referenced by current wire and so keeps being updated by current_wire
        current_wire = new_wire
        for point in points[1:]:
            child_wire = Wire(point, None)
            current_wire.add_child(child_wire)
            current_wire = child_wire

        self.wires[chunk_id].append(new_wire)