import json
import os
from typing import List
from insumos import Insumos
from cafe import Cafe
from cacao import Cacao
from lacteos import Lacteos


class CafeManager:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def save_cafe(self, cafe: List[Insumos]) -> None:
        try:
            # Se usa el método to_dict de cada objeto en la lista
            data = [insumo.to_dict() for insumo in cafe]
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
                print(f"✅ Datos guardados en {self.filename}")
        except IOError as e:
            print(f"❌ Error al guardar: {e}")

    def load_cafe(self) -> List[Insumos]:
        if not os.path.exists(self.filename):
            return []

        cafe_list = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data_list = json.load(f)
                for item in data_list:
                    if item["type"] == "Cafe":
                        obj = Cafe(item["brand"], item["model"], item["num_bags"])
                    elif item["type"] == "Cacao":
                        obj = Cacao(item["brand"], item["model"], item["total_kilos"])
                    elif item["type"] == "Lacteos":
                        obj = Lacteos(item["brand"], item["model"], item["es_deslact"])
                    else:
                        continue
                    cafe_list.append(obj)
            return cafe_list
        except (json.JSONDecodeError, KeyError):
            return []