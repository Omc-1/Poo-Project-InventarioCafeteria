from typing import Dict, Any
from insumos import Insumos


class Cafe(Insumos):
    def __init__(
        self,
        brand: str,
        model: str,
        num_bags: int,
        peso_por_costal_kg: float = 0.0,
        fecha_caducidad: str | None = None,
    ) -> None:
        super().__init__(brand, model)
        self.__num_bags = num_bags
        self.__peso_por_costal_kg = float(peso_por_costal_kg)
        self.__fecha_caducidad = fecha_caducidad

    @property
    def num_bags(self) -> int:
        return self.__num_bags

    @property
    def peso_por_costal_kg(self) -> float:
        return self.__peso_por_costal_kg

    @property
    def fecha_caducidad(self) -> str | None:
        return self.__fecha_caducidad

    def total_kilos(self) -> float:
        return self.__num_bags * self.__peso_por_costal_kg

    def move(self) -> str:
        cad = f" (caduca: {self.__fecha_caducidad})" if self.__fecha_caducidad else ""
        return (
            f"☕🫘 Cafe {self.brand} ({self.model}): "
            f"{self.__num_bags} costales, {self.__peso_por_costal_kg:.2f} kg por costal "
            f"(total {self.total_kilos():.2f} kg){cad}."
        )

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update(
            {
                "type": "Cafe",
                "num_bags": self.__num_bags,
                "peso_por_costal_kg": self.__peso_por_costal_kg,
                "fecha_caducidad": self.__fecha_caducidad,
            }
        )
        return data
