from typing import List

def game_help(help_type: str = "None") -> str:
    if help_type == "movement":
        return """
Movement:
    - left (l): Move left
    - right (r): Move right
    - up (u): Move up
    - down (d): Move down
"""
    elif help_type == "map":
        return """
Map:
    - @: wire
    - %: hub

    - f: fossil
    - c: coal
    - o: oil
    - g: gas

    - F: fossil generator
    - C: coal generator
    - O: oil generator
    - G: gas generator

    - #: solar panel
    - ~: wind turbine
"""
    else: return """
Commands:
    - For help with movment type: 'help movement'
    - For help with map keys type: 'help map'

    - 'shop': View the shop
    - 'buy <item>': Buy an item from the shop
    - 'exit': Quit the game!

About:
    To the play the game you must build resource generators and wire them up to the hub to earn money.

    Some generators need to be on their corrosponding resource deposits. (Type 'help map' for more info).
    They also need to be connected to a hub.

    You can have 1 hub in each chunk.
    Hubs can only have 1 wire on each square / of them (9x9).
    You can buy more chunks in the shop.

    Wires must begin on the same coordinates as the generator and end on the same coordinates of the part of the hub you want to attach it to.
"""

def left() -> str:
    return "l"

def right() -> str:
    return "r"

def up() -> str:
    return "u"

def down() -> str:
    return "d"

def parse_input(cmds: List) -> str:
    if len(cmds) == 0: return "Please enter a valid command... ('help' for more info)"
    
    if cmds[0] == "help":
        if len(cmds) > 1: return game_help(cmds[1])
        else: return game_help()
    
    elif cmds[0] == "exit": return "exit"

    elif cmds[0] == "shop": return "shop"
    elif cmds[0] == "buy":
        if len(cmds) > 1:
            if len(cmds[1]) > 0: return "store;buy_item|" + cmds[1]
            else: return "Please provide a valid item to buy... ('help' for more info)"
        else: return "Please provide a valid item to buy... ('help' for more info)"
    
    elif len(cmds) == 1 and len(cmds[0]) == 0: return ""

    elif cmds[0] == "l": return left()
    elif cmds[0] == "r": return right()
    elif cmds[0] == "u": return up()
    elif cmds[0] == "d": return down()
    else: return game_help()