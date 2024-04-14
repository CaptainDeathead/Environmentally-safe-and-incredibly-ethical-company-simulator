from typing import List
from Chunks.chunk_manager import ChunkManager
from data import *
from utils import *
from input_parser import parse_input
from Ui.table import table_from_2d_list
from Ui.hud import display_hud
from Ui.menus import MenuManager
from Construction.construction import ConstructionManager
from Chunks.chunk import Chunk

class Game:
    def __init__(self):
        self.chunk_manager: ChunkManager = ChunkManager()
        self.menu_manager: MenuManager = MenuManager()
        self.construction_manager: ConstructionManager = ConstructionManager()
        self.money = 1000
        self.income_rate = 0
        self.xp = 1

    def handle_ui_messages(self, cmds: List) -> str:
        if len(cmds) > 0: res = parse_input(cmds)
        else: res = ""
        if res in ("l", "r", "u", "d"):
            if res == "l": self.chunk_manager.move(-1, 0)
            elif res == "r": self.chunk_manager.move(1, 0)
            elif res == "u": self.chunk_manager.move(0, 1)
            elif res == "d": self.chunk_manager.move(0, -1)
            res = ""
        elif res == "exit": exit()
        elif res in list(self.menu_manager.action_bindings.keys()): res = self.menu_manager.find_and_draw_menu([res])
        elif ";" in res:
            res = res.split(";")
            if res[0] == "store" and res[1].split("|")[0] == "buy_item":
                item = res[1].split("|")[1]

                res = self.menu_manager.find_and_draw_menu(["buy", item])
                if res == "none": res = "Failed to buy item. Does not exist!\nType 'help' for more info...\n"
                else:
                    if self.money >= int(res):
                        self.money -= int(res)
                        res = f"Successfully purchased {item}!\n"
                        
                        if SHOP_ITEM_TYPES[item] == 0:
                            self.construction_manager.build(item, self.chunk_manager.chunks[1][1].chunk_id)

                    else: print("You do not have enough money to buy this item!\n")
        return res

    def main(self):
        cls()
        print(parse_input([""]))
        cmds: List = []
        res: str = ""
        while 1:
            cls()

            res = self.handle_ui_messages(cmds)

            print(display_hud(self.money, self.income_rate, self.xp, self.chunk_manager.position))

            curr_chunk: Chunk = self.chunk_manager.chunks[1][1]
            map_render: list = []

            # draw wires
            if curr_chunk.chunk_id in self.construction_manager.wires:
                curr_chunk_list = []
                for line in curr_chunk.chunk_map:
                    curr_chunk_list.append(list(line))

                for wire in self.construction_manager.wires[curr_chunk.chunk_id]:
                    for child_wire in wire.iterate_children():
                        curr_chunk_list[child_wire.location[1]][child_wire.location[0]] = SYMBOLS['wire']

                for line in curr_chunk_list:
                    map_render.append("".join(line))
            else:
                map_render = curr_chunk.chunk_map.copy()

            print(table_from_2d_list(map_render))
            print()

            print(res)

            cmds = input("Type 'help' for more info: ").lower().split(' ')