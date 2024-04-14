from typing import List
from Chunks.chunk_manager import ChunkManager
from data import *
from utils import *
from input_parser import parse_input
from Ui.table import table_from_2d_list
from Ui.hud import display_hud
from Ui.menus import MenuManager
from Construction.construction import ConstructionManager

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
                buy: bool = True
                while 1:
                    ammount = input("Ammount to purchase ('c' to cancel, 1 is the default: `enter`): ")
                    if ammount == 'c':
                        buy = False
                        break
                    elif ammount == "": ammount = 1

                    try:
                        ammount = int(ammount)
                        if ammount <= 0: print("Please enter an ammount greater than 0!")
                        else: break
                    except ValueError: print("Please enter a valid ammount!")

                if buy:
                    res = self.menu_manager.find_and_draw_menu(["buy", item, ammount])
                    if res == "none": res = "Failed to buy item. Does not exist!\nType 'help' for more info...\n"
                    else:
                        if self.money >= int(res):
                            self.money -= int(res)
                            res = f"Successfully purchased {ammount} {item}!\n"
                        else: print("You do not have enough money to buy this item!\n")
                else: res = ""
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

            print(table_from_2d_list(self.chunk_manager.chunks[1][1].chunk_map))
            print()

            print(res)

            cmds = input("Type 'help' for more info: ").lower().split(' ')