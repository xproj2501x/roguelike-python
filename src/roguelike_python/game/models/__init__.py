from enum import Enum


DEFAULT_WORLD_SIZE = 513

DEFAULT_ZONE_SIZE = 33


class LayerName(Enum):
    ELEVATION = 0
    TEMPERATURE = 1
    PRECIPITATION = 2
    EROSION = 3
    WATER_MAP = 4
    IRRIGATION = 5
    HUMIDITY = 6
    PERMEABILITY = 7
    BIOME = 8
    ICE_CAP = 9
    ZONE = 10


class ElevationKeys(Enum):
    DEEP_WATER = 0
    SHALLOW_WATER = 1
    COASTAL = 2
    PLAINS = 3
    HILLS = 4
    MOUNTAIN: 5
    ALPINE = 6
    SNOW_CAP = 7


class TemperatureKeys(Enum):
    ARCTIC = 0
    SUBARCTIC = 1
    BOREAL = 2
    TEMPERATE = 3
    SUBTROPICAL = 4
    TROPICAL = 5


class PrecipitationKeys(Enum):
    ARID = 0
    SEMIARID = 1
    MODERATE = 2
    HUMID = 3
    RAINY = 4