from data import SHOP_ITEMS, SHOP_ITEM_PRICES
from typing import Dict

class Shop:
    def __init__(self):
        self.action_bindings: Dict = {
            'view': self.view_shop
        }

    def view_shop(self) -> str:
        ret_str: str = "Shop:"
        
        for item in SHOP_ITEMS:
            ret_str += f"\n    - {item}: ${str(SHOP_ITEM_PRICES[item])}"

        return ret_str + "\n"
    
    def buy_item(self, item: str) -> tuple:
        if item in SHOP_ITEMS:
            # DOES NOT CHECK IF ENOUGH MONEY
            return str(SHOP_ITEM_PRICES[item])
        else: return "none"