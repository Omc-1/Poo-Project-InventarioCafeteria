from typing import Dict, Any
from insumos import Insumos

class Lacteos(Insumos):
    """Clase hija lacteos"""

    def __init__(self, brand: str, model: str, es_deslact: bool) -> None:
        super().__init__(brand, model)
        self.__es_deslact = es_deslact

    def move(self) -> str:
        tipo = "La leche deslactosada" if self.__es_deslact else "La leche entera"
        return f"🥛 🐄 {tipo} {self.brand} llega desde granjas locales y se almacena bajo refrigeracion."

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "type": "Lacteos",
            "es_deslact": self.__es_deslact
        })
        return data