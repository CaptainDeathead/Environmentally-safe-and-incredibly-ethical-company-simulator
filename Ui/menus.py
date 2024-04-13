from Ui.shop import Shop
from typing import Dict

class MenuManager:
    def __init__(self):
        self.shop: Shop = Shop()

        self.action_bindings: Dict = {
            'shop': self.shop.action_bindings['view']
        }

    def find_and_draw_menu(self, cmd: str) -> str:
        if cmd in self.action_bindings: return self.action_bindings[cmd]()
        else: raise Exception(f"No menu found for '{cmd}'!")