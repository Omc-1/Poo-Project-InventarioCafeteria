from typing import Dict, Any
from insumos import Insumos


class Cacao(Insumos):
    def __init__(
        self,
        brand: str,
        model: str,
        total_kilos: float,
        fecha_caducidad: str | None = None,
    ) -> None:
        super().__init__(brand, model)
        self.__total_kilos = total_kilos
        self.__fecha_caducidad = fecha_caducidad

    @property
    def fecha_caducidad(self) -> str | None:
        return self.__fecha_caducidad

    def move(self) -> str:
        cad = f" (caduca: {self.__fecha_caducidad})" if self.__fecha_caducidad else ""
        return f"🍫🌰 El chocolate {self.brand} almacenado en bodega son {self.__total_kilos} kilos{cad}."

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update(
            {
                "type": "Cacao",
                "total_kilos": self.__total_kilos,
                "fecha_caducidad": self.__fecha_caducidad,
            }
        )
        return data
