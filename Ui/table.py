from typing import List
from data import SYMBOLS

def table_from_2d_list(inp_list: List) -> str:
    if len(inp_list) == 0 or len(inp_list[0]) == 0:
        raise Exception("Cannot provide list with elements that have a length equal to 0!")
    
    output: List = []
    size_x: int = len(inp_list[0])
    size_y: int = len(inp_list[1])

    for y in range(size_y):
        output.append("")
        for x in range(size_x):
            output[y] += ' ' + inp_list[y][x]

    return "\n".join(output)