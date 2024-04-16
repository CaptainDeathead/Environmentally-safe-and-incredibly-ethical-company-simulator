from typing import Dict, List, Tuple
from Construction.wire import Wire
from Construction.generators import SolarPanel, WindTurbine
from data import CHUNK_SIZE, CHUNK_CENTER

class ConstructionManager:
    def __init__(self):
        self.wires: Dict = {}
        self.chunk_connectors: List = []
        self.hubs: Dict = {}
        self.extractors: Dict = {}
        self.generators: Dict = {}

    def wire_connects_hub(self, wire: Wire, chunk_id: int) -> Tuple:
        if chunk_id not in self.hubs: return (9, 9)

        children: List = list(wire.iterate_children())
        
        if len(children) > 0: wire_end = children[-1]
        else: wire_end = wire

        for y in range(-1, 2):
            for x in range(-1, 2):
                node_location: Tuple = (CHUNK_CENTER+x, CHUNK_CENTER+y)
                if self.hubs[chunk_id].nodes[y][x] is False and wire_end.location == node_location:
                    return (x, y)
                
        return (9, 9)

    def build(self, item, chunk_id: int = None, draw_map_func = None, cls = None):
        if item == 'wire': self.place_wire(chunk_id, draw_map_func, cls)
        elif item in ("solar_panel", "wind_turbine"): self.place_generator(chunk_id, item, draw_map_func, cls)

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

            if new_point_x > CHUNK_SIZE or new_point_y > CHUNK_SIZE:
                cls()
                print(f"Please make sure coordinates are between 1 and {CHUNK_SIZE}")
                continue

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

    def place_generator(self, chunk_id: int, generator_type: str, draw_map_func, cls):
        while 1:
            print(f"Building: {generator_type}\n")
            draw_map_func()
            new_point: str = input(f"Enter the coordinates in ('x,y' | e.g. '1,3') format between 1 and {CHUNK_SIZE}: ")

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

            if new_point_x > CHUNK_SIZE or new_point_y > CHUNK_SIZE:
                cls()
                print(f"Please make sure coordinates are between 1 and {CHUNK_SIZE}")
                continue

            if chunk_id not in self.generators:
                if generator_type == 'solar_panel': self.generators[chunk_id] = [SolarPanel(chunk_id, (new_point_x, new_point_y))]
                elif generator_type == 'wind_turbine': self.generators[chunk_id] = [WindTurbine(chunk_id, (new_point_x, new_point_y))]
            else:
                if generator_type == 'solar_panel': self.generators[chunk_id].append(SolarPanel(chunk_id, (new_point_x, new_point_y)))
                elif generator_type == 'wind_turbine': self.generators[chunk_id].append(WindTurbine(chunk_id, (new_point_x, new_point_y)))

            cls()
            break

    def connect_wires(self, chunk_id: int):
        if chunk_id not in self.hubs: return
        
        self.hubs[chunk_id].reset_nodes()

        if chunk_id not in self.generators: return

        for generator in self.generators[chunk_id]:
            generator.connected = False
            if chunk_id not in self.wires: return
            for chained_wire in self.wires[chunk_id]:
                x, y = self.wire_connects_hub(chained_wire, chunk_id)
                if x != 9:
                    for wire in chained_wire.iterate_children():
                        if wire.location == generator.location:
                            self.hubs[chunk_id].nodes[y][x] = True
                            generator.connected = True