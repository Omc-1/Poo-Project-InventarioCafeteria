import os
from datetime import datetime
from typing import List
from cafe import Cafe
from cacao import Cacao
from lacteos import Lacteos, mostrar_total_litros_leche
from data import CafeManager
from insumos import Insumos


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pedir_fecha_caducidad() -> str | None:
    while True:
        raw = input("Fecha de caducidad (DD-MM-YYYY) [enter si no aplica]: ").strip()
        if raw == "":
            return None
        try:
            datetime.strptime(raw, "%d-%m-%Y")
            return raw
        except ValueError:
            print("Formato inválido. Usa DD-MM-YYYY (ej: 10-04-2026).")


def display():
    manager = CafeManager("Inventario_cafe.json")
    cafe_inv: List[Insumos] = manager.load_cafe()

    while True:
        clear_screen()
        print("***** INVENTARIO DE CAFETERIA *****")
        print(f"Productos en bodega: {len(cafe_inv)}")
        print("1. Agregar productos cafe")
        print("2. Agregar productos cacao")
        print("3. Agregar productos lacteos")
        print("4. Ver inventario (Polimorfismo)")
        print("5. Guardar y salir")

        option = input("\nSelecciona una opcion: ")

        if option in ["1", "2", "3"]:
            brand = input("Marca: ")
            model = input("Presentacion: ")

            if option == "1":
                bags = int(input("Numero de costales en existencia: "))
                peso_costal = float(input("Peso por costal (kg): "))
                fecha = pedir_fecha_caducidad()
                cafe_inv.append(Cafe(brand, model, bags, peso_costal, fecha))
            elif option == "2":
                kilos = float(input("Kilos en almacen: "))
                fecha = pedir_fecha_caducidad()
                cafe_inv.append(Cacao(brand, model, kilos, fecha))
            elif option == "3":
                deslac = input("¿Es deslactosada? (si/no): ").lower() == "si"
                litros = float(input("Litros almacenados: "))
                fecha = pedir_fecha_caducidad()
                cafe_inv.append(Lacteos(brand, model, deslac, litros, fecha))

            print("✅ ¡Producto agregado!")
            input("Presione enter para continuar...")

        elif option == "4":
            print("\n*** INVENTARIO EN BODEGA ***")
            if not cafe_inv:
                print("La bodega esta vacia.")
            else:
                for idx, v in enumerate(cafe_inv, 1):
                    # Polimorfismo: cada objeto responde con su propio método move()
                    print(f"{idx}. {v.brand}, {v.model} -> {v.move()}")

                lacteos_items = [i for i in cafe_inv if isinstance(i, Lacteos)]
                if lacteos_items:
                    mostrar_total_litros_leche(lacteos_items)
            input("\nPresione enter para continuar...")

        elif option == "5":
            manager.save_cafe(cafe_inv)
            print("Inventario terminado. Saliendo...")
            break
        else:
            print("Opción no válida.")
            input("Presione enter para intentar de nuevo...")
