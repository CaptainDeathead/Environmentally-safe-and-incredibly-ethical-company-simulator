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
from Construction.hub import Hub
from time import time

class Game:
    def __init__(self):
        self.chunk_manager: ChunkManager = ChunkManager()
        self.menu_manager: MenuManager = MenuManager()
        self.construction_manager: ConstructionManager = ConstructionManager()
        self.construction_manager.hubs[self.chunk_manager.chunks[1][1].chunk_id] = Hub(self.chunk_manager.chunks[1][1].chunk_id)
        self.money = 60000000
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
                        money_before = self.money
                        self.money -= int(res)

                        res = f"Successfully purchased {item}!\n"

                        if SHOP_ITEM_TYPES[item] == 0:
                            len_generators_before = len(self.construction_manager.generators)
                            self.construction_manager.build(item, self.chunk_manager.chunks[1][1].chunk_id, self.draw_map, cls)

                            if len(self.construction_manager.generators) == len_generators_before:
                                res = "You have been refunded!\n"
                                self.money = money_before

                            self.construction_manager.connect_wires(self.chunk_manager.chunks[1][1].chunk_id)

                    else: print("You do not have enough money to buy this item!\n")
        return res
    
    def draw_map(self) -> list:
        curr_chunk: Chunk = self.chunk_manager.chunks[1][1]
        map_render: list = []
        curr_chunk_list: list = []

        for line in curr_chunk.chunk_map:
            curr_chunk_list.append(list(line))

        # draw wires
        if curr_chunk.chunk_id in self.construction_manager.wires:
            for wire in self.construction_manager.wires[curr_chunk.chunk_id]:
                if wire == None: continue
                for child_wire in wire.iterate_children():
                    curr_chunk_list[child_wire.location[1]][child_wire.location[0]] = SYMBOLS['wire']
                
        # draw generators
        if curr_chunk.chunk_id in self.construction_manager.generators:
            for generator in self.construction_manager.generators[curr_chunk.chunk_id]:
                curr_chunk_list[generator.location[1]][generator.location[0]] = SYMBOLS[generator.GENERATOR_TYPE]

        # draw hub
        if curr_chunk.chunk_id in self.construction_manager.hubs:
            for y in range(-1, 2):
                for x in range(-1, 2):
                    curr_chunk_list[CHUNK_CENTER+y][CHUNK_CENTER+x] = SYMBOLS['hub']

        map_render_list = curr_chunk_list.copy()

        for line in curr_chunk_list:
            map_render.append("".join(line))

        print(table_from_2d_list(map_render))
        print()

        return map_render_list

    def main(self):
        cls()
        print(parse_input([""]))
        cmds: List = []
        res: str = ""
        last_time = time()
        while 1:
            cls()

            if self.chunk_manager.chunks[1][1].chunk_id in self.construction_manager.generators:
                for generator in self.construction_manager.generators[self.chunk_manager.chunks[1][1].chunk_id]:
                    if not generator.connected: continue
                    self.money += POWER_OUTPUTS[generator.GENERATOR_TYPE]*(time()-last_time)/100

            last_time = time()

            res = self.handle_ui_messages(cmds)

            print(display_hud(int(round(self.money, 0)), self.income_rate, self.xp, self.chunk_manager.position))

            self.draw_map()

            print(res)

            cmds = input("Type 'help' for more info: ").lower().split(' ')