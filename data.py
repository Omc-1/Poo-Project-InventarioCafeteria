import json
import os
from datetime import datetime
from typing import List
from insumos import Insumos
from cafe import Cafe
from cacao import Cacao
from lacteos import Lacteos


def normalizar_fecha_caducidad(raw: str | None) -> str | None:
    if not raw:
        return None

    # Formato nuevo esperado: DD-MM-YYYY
    try:
        datetime.strptime(raw, "%d-%m-%Y")
        return raw
    except ValueError:
        pass

    # Compatibilidad con formato antiguo: YYYY-MM-DD
    try:
        dt = datetime.strptime(raw, "%Y-%m-%d")
        return dt.strftime("%d-%m-%Y")
    except ValueError:
        return raw


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
                        obj = Cafe(
                            item["brand"],
                            item["model"],
                            item["num_bags"],
                            item.get("peso_por_costal_kg", 0.0),
                            normalizar_fecha_caducidad(item.get("fecha_caducidad")),
                        )
                    elif item["type"] == "Cacao":
                        obj = Cacao(
                            item["brand"],
                            item["model"],
                            item["total_kilos"],
                            normalizar_fecha_caducidad(item.get("fecha_caducidad")),
                        )
                    elif item["type"] == "Lacteos":
                        obj = Lacteos(
                            item["brand"],
                            item["model"],
                            item["es_deslact"],
                            item.get("litros", 0.0),
                            normalizar_fecha_caducidad(item.get("fecha_caducidad")),
                        )
                    else:
                        continue
                    cafe_list.append(obj)
            return cafe_list
        except (json.JSONDecodeError, KeyError):
            return []
