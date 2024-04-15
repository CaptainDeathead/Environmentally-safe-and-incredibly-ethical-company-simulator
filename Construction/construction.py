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

    def build(self, item, chunk_id: int = None, draw_map_func = None, cls = None):
        if item == 'wire': self.place_wire(chunk_id, draw_map_func, cls)

    def place_wire(self, chunk_id: int, draw_map_func, cls):
        points: List = []
        
        point_type: str = "first"

        # add the chunk to the wires dict
        if chunk_id not in self.wires:
            self.wires[chunk_id] = []

        self.wires[chunk_id].append(None)

        while 1:
            print("Building: wire\n")
            draw_map_func()
            new_point: str = input(f"Enter the {point_type} point in ('x,y' | e.g. '1,3') format between 1 and {CHUNK_SIZE} ('c' to end wire): ")

            if new_point == 'c':
                cls()
                break

            if ',' not in new_point:
                cls()
                print("Incorrect format! Make sure you have a comma.")
                continue
            
            new_point_x, new_point_y = new_point.split(',')
            new_point_x = new_point_x.replace(' ', '')
            new_point_y = new_point_y.replace(' ', '')

            if not (new_point_x.isdigit() and new_point_y.isdigit()):
                cls()
                print("Please make sure your coordinates are valid whole numbers!")
                continue

            new_point_x = int(new_point_x)-1
            new_point_y = int(new_point_y)-1

            if point_type == "next":
                new_wire_and_children = list(new_wire.iterate_children())
                new_wire_and_children.insert(0, new_wire)
                
                if new_wire_and_children[-1].location == (new_point_x, new_point_y):
                    cls()
                    print("You just entered that point, try a different one!")
                    continue

                # check if wire already exists at the new point
                collides = False
                for wire in new_wire_and_children:
                    if wire.location == (new_point_x, new_point_y):
                        cls()
                        print("You've already entered that point, try a different one!")
                        collides = True
                        break

                if collides: continue

                filling_x: bool = new_point_y == new_wire_and_children[-1].location[1] # if the current y is equal to the last y we are filling x
                if (filling_x and new_point_y != new_wire_and_children[-1].location[1]) or ((not filling_x) and new_point_x != new_wire_and_children[-1].location[0]):
                    cls()
                    print("Please ensure you enter the coordinates on either the x or y axis but not both so that the wires are in streight lines!\ne.g. The previous point was '2,2' then the next point has to be something like: '5,2' or '2,1' not '3, 6' because it would be diagonal.")
                    continue
                elif filling_x:
                    last_wire_location_x = new_wire_and_children[-1].location[0]
                    
                    x1 = last_wire_location_x
                    x2 = new_point_x + 1

                    if last_wire_location_x < new_point_x+1:
                        step = 1
                    else:
                        x2 -= 2
                        step = -1

                    for x in range(x1, x2, step):
                        # new wire will contain a reference to current_wire (they reference the same object)
                        # basicly new_wire is a reference to the initial wire created, and has current_wire keeps walking further and further, new_wire still contains the reference to the starting wire, which is also referenced by current wire and so keeps being updated by current_wire
                        child_wire = Wire((x, new_point_y), None)
                        current_wire.add_child(child_wire)
                        current_wire = child_wire
                else:
                    last_wire_location_y = new_wire_and_children[-1].location[1]
                    
                    y1 = last_wire_location_y
                    y2 = new_point_y + 1

                    if last_wire_location_y < new_point_y+1:
                        step = 1
                    else:
                        y2 -= 2
                        step = -1

                    for y in range(y1, y2, step):
                        child_wire = Wire((new_point_x, y), None)
                        current_wire.add_child(child_wire)
                        current_wire = child_wire

            else:
                new_wire: Wire = Wire((new_point_x, new_point_y), None)
                current_wire: Wire = new_wire

            self.wires[chunk_id][-1] = new_wire
            point_type = "next"
            cls()