from typing import Tuple

def render_money(money: int) -> str:
    return "$" + str(money)

def render_income_rate(income_rate: int) -> str:
    return "$" + str(income_rate) + "/s"

def render_xp(xp: int) -> str:
    return "XP: " + str(xp)

def render_direction_to_center(direction_to_center: Tuple) -> str:
    # find the smaller out of x and y
    abs_x = abs(direction_to_center[0])
    abs_y = abs(direction_to_center[1])

    if abs_x != 0 and (abs_y == 0 or abs_x <= abs_y):
        if direction_to_center[0] > 0: return "<"
        elif direction_to_center[0] < 0: return ">"
        else: return "+"
    else:
        if direction_to_center[1] > 0: return "v"
        elif direction_to_center[1] < 0: return "^"
        else: return "+"

def display_hud(money: int, income_rate: int, xp: int, direction_to_center: Tuple) -> str:
    hud_text: str = ""
    layer_1 = " "
    layer_2 = "|"

    # money
    money_str: str = render_money(money)

    for _ in range(len(money_str)+3): layer_1 += "-"

    layer_2 += " {} ".format(money_str) + "|"

    # income rate
    income_rate_str: str = render_income_rate(income_rate)

    for _ in range(len(income_rate_str)+3): layer_1 += "-"

    layer_2 += " {} ".format(income_rate_str) + "|"

    # xp
    xp_str: str = render_xp(xp)

    for _ in range(len(xp_str)+3): layer_1 += "-"

    layer_2 += " {} ".format(xp_str) + "|"

    # direction to center
    direction_to_center_str: str = render_direction_to_center(direction_to_center)

    for _ in range(len(direction_to_center_str)+2): layer_1 += "-"

    layer_2 += " {} ".format(direction_to_center_str) + "|"

    return layer_1 + "\n" + layer_2 + "\n" + layer_1