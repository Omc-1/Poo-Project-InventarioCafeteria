import json
import os
from insumos import Insumos
from cafe import Cafe
from cacao import Cacao
from lacteos import Lacteos

class CafeManager:
    def __init__(self, file_path: str = "inventario_cafe.json"):
        self.file_path = file_path

    def save_data(self, cafe_list: list[Insumos]) -> None:
        data = []
        for cafe in cafe_list:
            # Diccionario base con atributos comunes
            item = {
                "brand": cafe.brand,
                "model": cafe.model,
                "type": cafe.__class__.__name__,
                "bags": cafe.bags
            }
            # Atributos específicos por clase
            if isinstance(cafe, Cafe):
                item["kilos_per_bag"] = cafe.kilos_per_bag
            elif isinstance(cafe, Cacao):
                item["kilos_per_bag"] = cafe.kilos_per_bag
            elif isinstance(cafe, Lacteos):
                item["liters_per_bag"] = cafe.liters_per_bag
            
            data.append(item)

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self) -> list[Insumos]:
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as f:
            data = json.load(f)

        # CORRECCIÓN CLAVE: Anotar la lista como list[Insumos] 
        # para que acepte cualquier subclase sin errores de invarianza.
        cafe_list: list[Insumos] = []
        
        for item in data:
            brand = item["brand"]
            model = item["model"]
            type_name = item["type"]
            bags = item["bags"]

            # CORRECCIÓN CLAVE: Usar el tipo 'Insumos' para la variable temporal
            # Esto permite el polimorfismo que Mypy estaba bloqueando.
            producto: Insumos

            if type_name == "Cafe":
                kilos_per_bag = item["kilos_per_bag"]
                producto = Cafe(brand, model, type_name, bags, kilos_per_bag)
            elif type_name == "Cacao":
                kilos_per_bag = item["kilos_per_bag"]
                producto = Cacao(brand, model, type_name, bags, kilos_per_bag)
            elif type_name == "Lacteos":
                liters_per_bag = item["liters_per_bag"]
                producto = Lacteos(brand, model, type_name, bags, liters_per_bag)
            else:
                continue
                
            cafe_list.append(producto)

        return cafe_list
