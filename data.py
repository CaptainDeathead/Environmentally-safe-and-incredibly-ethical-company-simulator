

CHUNK_SIZE: int = 18
CHUNK_CENTER: int = int(CHUNK_SIZE/2)
SEED: int = 15

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
    'wind_turbine': '~',

    'fossil_generator': 'F',
    'coal_generator': 'C',
    'oil_generator': 'O',
    'gas_generator': 'G'
}

GENERATOR_DEPOSITS = {
    'fossil_generator': 'fossil',
    'coal_generator': 'coal',
    'oil_generator': 'oil',
    'gas_generator': 'gas'
}

SHOP_ITEMS = ['wire', 'solar_panel', 'wind_turbine', 'fossil_generator', 'coal_generator', 'oil_generator', 'gas_generator']

SHOP_ITEM_PRICES = {
    'wire': 0,
    'solar_panel': 5000,
    'wind_turbine': 15000,
    'fossil_generator': 40_000,
    'coal_generator': 100_000,
    'oil_generator': 220_000,
    'gas_generator': 500_000
}

SHOP_ITEM_TYPES = {
    'wire': 0,
    'solar_panel': 0,
    'wind_turbine': 0,
    'fossil_generator': 0,
    'coal_generator': 0,
    'oil_generator': 0,
    'gas_generator': 0
}

SHOP_ITEM_TYPES_TO_STR = {
    0: 'constructable'
}

POWER_OUTPUTS = {
    'solar_panel': 250,
    'wind_turbine': 900,
    'fossil_generator': 2400,
    'coal_generator': 9200,
    'oil_generator': 21_300,
    'gas_generator': 54_600
}