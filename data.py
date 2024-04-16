

CHUNK_SIZE: int = 18
CHUNK_CENTER: int = int(CHUNK_SIZE/2)
SEED: int = 314159

DEPOSIT_TYPES = ['none', 'fossil', 'coal', 'oil', 'gas']

DEPOSIT_SPAWN_CHANCES = { # higher is better
    'none': 8000,
    'fossil': 20,
    'coal': 10,
    'oil': 6,
    'gas': 2
}

SYMBOLS = {
    'none': '.',
    'fossil': 'f',
    'coal': 'c',
    'oil': 'o',
    'gas': 'g',

    'hub': '%',
    'wire': '@',
    'solar_panel': '#',
    'wind_turbine': '~'
}

SHOP_ITEMS = ['wire', 'solar_panel', 'wind_turbine']

SHOP_ITEM_PRICES = {
    'wire': 0,
    'solar_panel': 5000,
    'wind_turbine': 15000
}

SHOP_ITEM_TYPES = {
    'wire': 0,
    'solar_panel': 0,
    'wind_turbine': 0
}

SHOP_ITEM_TYPES_TO_STR = {
    0: 'constructable'
}

POWER_OUTPUTS = {
    'solar_panel': 250,
    'wind_turbine': 900
}