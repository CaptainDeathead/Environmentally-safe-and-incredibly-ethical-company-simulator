from typing import List
from Chunks.chunk_manager import ChunkManager
from data import *
from utils import *
from input_parser import parse_input
from Ui.table import table_from_2d_list
from Ui.hud import display_hud

class Game:
    def __init__(self):
        self.chunk_manager: ChunkManager = ChunkManager()
        self.money = 1000
        self.income_rate = 0
        self.xp = 1

    def main(self):
        cls()
        print(parse_input([""]))
        cmds: List = []
        res: str = ""
        while 1:
            cls()

            if len(cmds) > 0: res = parse_input(cmds)
            else: res = ""
            if res in ("l", "r", "u", "d"):
                if res == "l": self.chunk_manager.move(-1, 0)
                elif res == "r": self.chunk_manager.move(1, 0)
                elif res == "u": self.chunk_manager.move(0, 1)
                elif res == "d": self.chunk_manager.move(0, -1)
                res = ""
            elif res == "exit": exit()

            print(display_hud(self.money, self.income_rate, self.xp, self.chunk_manager.position))

            print(table_from_2d_list(self.chunk_manager.chunks[1][1].chunk_map))
            print()

            print(res)

            cmds = input("Type 'help' for more info: ").lower().split(' ')