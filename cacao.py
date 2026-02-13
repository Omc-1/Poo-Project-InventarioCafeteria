from typing import Dict, Any
from insumos import Insumos

class Cacao(Insumos):
    def __init__(self, brand: str, model: str, total_kilos: float) -> None:
        super().__init__(brand, model)
        self.__total_kilos = total_kilos

    def move(self) -> str:
        return f"🍫🌰 El chocolate {self.brand} almacenado en bodega son {self.__total_kilos} kilos."

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "type": "Cacao",
            "total_kilos": self.__total_kilos
        })
        return data