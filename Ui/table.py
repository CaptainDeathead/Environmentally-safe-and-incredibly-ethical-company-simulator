from typing import List
from data import SYMBOLS

def table_from_2d_list(inp_list: List) -> str:
    if len(inp_list) == 0 or len(inp_list[0]) == 0:
        raise Exception("Cannot provide list with elements that have a length equal to 0!")
    
    output: List = ["                             10+\n                      -----------------\n    1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9\n1  "]
    size_x: int = len(inp_list[0])
    size_y: int = len(inp_list[1])

    for y in range(size_y):
        if y < 8: output.append(f"{y+2}  ")
        else: output.append(f"{y+2} ")
        for x in range(size_x):
            output[y] += ' ' + inp_list[y][x]

    return "\n".join(output)