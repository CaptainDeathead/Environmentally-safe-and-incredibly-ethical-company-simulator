from os import system, name
from random import seed
from data import SEED

shown_platform_error: bool = False
seed(SEED)

def cls():
    global shown_platform_error
    # windows
    if name == 'nt': system('cls')
    else:
        system('clear')
        if not shown_platform_error:
            print(f"Device platform recognised as: '{name}'.\nUsing 'clear' as the default command to clear screen.\n\nThis message will not be shown again.\n")
            shown_platform_error = True

def unique_number_from_pair(a, b):
    return hash((a, b))

def rgb_to_ansi(r: int, g: int, b: int, string: str):
    return f"\033[38;2;{r};{g};{b}m{string}\033[0m"