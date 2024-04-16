from typing import Tuple
from Construction.wire import Wire

class SolarPanel:
    def __init__(self, chunk_id: int, location: Tuple):
        self.chunk_id = chunk_id
        self.location = location
        self.connected: bool = False
        self.DEPENDS_ON_EXTRACTOR: bool = False
        self.GENERATOR_TYPE: str = 'solar_panel'

class WindTurbine:
    def __init__(self, chunk_id: int, location: Tuple):
        self.chunk_id = chunk_id
        self.location = location
        self.connected: bool = False
        self.DEPENDS_ON_EXTRACTOR: bool = False
        self.GENERATOR_TYPE: str = 'wind_turbine'


# --------------------------- THIS CODE WILL BE MOVED TO EXTRACTORS LATER AND AN EXTRACTOR WILL NEED ITS CORROSPONDING GENERATOR TO FUNCTION ---------------------------

class FossilGenerator:
    def __init__(self, chunk_id: int, location: Tuple):
        self.chunk_id = chunk_id
        self.location = location
        self.connected: bool = False
        self.DEPENDS_ON_EXTRACTOR: bool = False
        self.GENERATOR_TYPE: str = 'fossil_generator'

class CoalGenerator:
    def __init__(self, chunk_id: int, location: Tuple):
        self.chunk_id = chunk_id
        self.location = location
        self.connected: bool = False
        self.DEPENDS_ON_EXTRACTOR: bool = False
        self.GENERATOR_TYPE: str = 'coal_generator'

class OilGenerator:
    def __init__(self, chunk_id: int, location: Tuple):
        self.chunk_id = chunk_id
        self.location = location
        self.connected: bool = False
        self.DEPENDS_ON_EXTRACTOR: bool = False
        self.GENERATOR_TYPE: str = 'oil_generator'

class GasGenerator:
    def __init__(self, chunk_id: int, location: Tuple):
        self.chunk_id = chunk_id
        self.location = location
        self.connected: bool = False
        self.DEPENDS_ON_EXTRACTOR: bool = False
        self.GENERATOR_TYPE: str = 'gas_generator'