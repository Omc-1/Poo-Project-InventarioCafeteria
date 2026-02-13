from typing import Dict, Any
from insumos import Insumos


class Cafe(Insumos):
    def __init__(self, brand: str, model: str, num_bags: int) -> None:
        super().__init__(brand, model)
        self.__num_bags = num_bags

    def move(self) -> str:
        return f"☕🫘 El cafe {self.brand} es transportado en camiones hasta el almacen."

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "type": "Cafe",
            "num_bags": self.__num_bags
        })
        return data


