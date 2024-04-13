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
    - f: fossil
    - c: coal
    - o: oil
    - g: gas"""
    else: return """
Commands:
    - For help with movment type: 'help movement'
    - For help with map keys type: 'map help'

    - 'exit': Quit the game!

    - More to come...
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
    
    elif len(cmds) == 1 and len(cmds[0]) == 0: return ""

    elif cmds[0] == "l": return left()
    elif cmds[0] == "r": return right()
    elif cmds[0] == "u": return up()
    elif cmds[0] == "d": return down()
    else: return game_help()