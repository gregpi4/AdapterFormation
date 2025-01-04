from dataclasses import dataclass

@dataclass
class Product:
    name: str
    energy: str
    protein: float
    fiber: float
    fat: float
    nutriscore: str
