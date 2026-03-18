from typing import Dict, Any
from insumos import Insumos

class Lacteos(Insumos):
    """Clase hija lacteos"""

    def __init__(
        self,
        brand: str,
        model: str,
        es_deslact: bool,
        litros: float = 0.0,
        fecha_caducidad: str | None = None,
    ) -> None:
        super().__init__(brand, model)
        self.__es_deslact = es_deslact
        self.__litros = float(litros)
        self.__fecha_caducidad = fecha_caducidad

    @property
    def litros(self) -> float:
        return self.__litros

    @property
    def fecha_caducidad(self) -> str | None:
        return self.__fecha_caducidad

    def move(self) -> str:
        tipo = "La leche deslactosada" if self.__es_deslact else "La leche entera"
        cad = f" (caduca: {self.__fecha_caducidad})" if self.__fecha_caducidad else ""
        return f"🥛 🐄 {tipo} {self.brand} debe ser almacenada bajo refrigeracion{cad}."

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "type": "Lacteos",
            "es_deslact": self.__es_deslact,
            "litros": self.__litros,
            "fecha_caducidad": self.__fecha_caducidad,
        })
        return data


def total_litros_leche(items: list[Lacteos]) -> float:
    return sum(i.litros for i in items)


def mostrar_total_litros_leche(items: list[Lacteos]) -> None:
    total = total_litros_leche(items)
    print(f"Total de litros de leche almacenados: {total:.2f} L")
