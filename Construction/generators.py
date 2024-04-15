from typing import Tuple
from Construction.wire import Wire

class SolarPanel:
    def __init__(self, chunk_id: int, location: Tuple):
        self.chunk_id = chunk_id
        self.location = location
        self.wire: Wire = None
        self.DEPENDS_ON_EXTRACTOR: bool = False
        self.GENERATOR_TYPE: str = 'solar_panel'