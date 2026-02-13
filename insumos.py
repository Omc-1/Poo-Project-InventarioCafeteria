from abc import abstractmethod
from typing import Dict, Any
from interface import ISerializable


class Insumos(ISerializable):
    def __init__(self, brand: str, model: str) -> None:
        self.__brand = brand
        self.__model = model  # Corregido de '-' a '='

    @property
    def brand(self) -> str:
        return self.__brand

    @property
    def model(self) -> str:
        return self.__model

    @abstractmethod
    def move(self) -> str:
        pass

    def to_dict(self) -> Dict[str, Any]:
        return {
            "brand": self.__brand,
            "model": self.__model
        }