from Ui.shop import Shop
from typing import Dict, List

class MenuManager:
    def __init__(self):
        self.shop: Shop = Shop()

        self.action_bindings: Dict = {
            'shop': self.shop.action_bindings['view']
        }

    def find_and_draw_menu(self, cmd: List) -> str:
        if cmd[0] in self.action_bindings: return self.action_bindings[cmd[0]]()
        elif cmd[0] == "buy": return self.shop.buy_item(cmd[1], cmd[2])
        else: raise Exception(f"No menu found for '{cmd[0]}'!")