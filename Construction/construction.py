from typing import List
from wire import Wire

class ConstructionManager:
    def __init__(self):
        self.wires: List = []
        self.chunk_connectors: List = []
        self.hubs: List = []
        self.extractors: List = []
        self.generators: List = []

    def place_wire(self):
        points: List = []
        
        print("Building: wire\n")
        
        point_type: str = "first"

        while 1:
            new_point: str = input("Enter the {} point in ('x,y' | e.g. '1,3') format ('c' to cancell): ", point_type)

            if new_point == 'c': break

            if ',' not in new_point:
                print("Incorrect format! Make sure you have a comma.")
                continue
            
            new_point_x, new_point_y = new_point.split(',')
            new_point_x.replace(' ', '')
            new_point_y.replace(' ', '')

            if not (new_point_x.isdigit() and new_point_y.isdigit()):
                print("Please make sure your coordinates are valid whole numbers!")
                continue
            
            points.append((new_point_x, new_point_y))

            point_type = "next"

        if len(points) == 0: return
        
        if len(points) == 1:
            self.wires.append(Wire(points[0], None))
            return
        
        if len(points) == 2:
            self.wires.append(Wire(points[0], Wire(points[1], None)))
            return
        
        new_wire = Wire(points[0])

        # new wire will contain a reference to current_wire (they reference the same object)
        # basicly new_wire is a reference to the initial wire created, and has current_wire keeps walking further and further, new_wire still contains the reference to the starting wire, which is also referenced by current wire and so keeps being updated by current_wire
        current_wire = new_wire
        for point in points[1:]:
            child_wire = Wire(point)
            current_wire.add_child(child_wire)
            current_wire = child_wire

        self.wires.append(new_wire)