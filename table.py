from typing import List
from data import SYMBOLS

def table_from_2d_list(inp_list: List) -> str:
    if len(inp_list) == 0 or len(inp_list[0]) == 0:
        raise Exception("Cannot provide list with elements that have a length equal to 0!")
    
    #output: List = ["\033[4m"]
    output: List = []
    size_x: int = len(inp_list[0])
    size_y: int = len(inp_list[1])

    # draw the top line
    #for x in range(size_x+1):
    #    output[0] += " "
    #
    #output[0] += "\033[0m"

    # draw the contents with underlines
    for y in range(size_y):
        output.append("")
        for x in range(size_x):
            output[y] += inp_list[y][x]

    # draw bottom line
    #output.append("\033[4m|")
    #for x in range(size_x+1):
    #    output[-1] += " "
    #
    #output[-1] += "\033[0m|"

    return "\n".join(output)