import os
from typing import List
from cafe import Cafe
from cacao import Cacao
from lacteos import Lacteos
from data import CafeManager
from insumos import Insumos


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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
                cafe_inv.append(Cafe(brand, model, bags))
            elif option == "2":
                kilos = float(input("Kilos en almacen: "))
                cafe_inv.append(Cacao(brand, model, kilos))
            elif option == "3":
                deslac = input("¿Es deslactosada? (si/no): ").lower() == 'si'
                cafe_inv.append(Lacteos(brand, model, deslac))

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
            input("\nPresione enter para continuar...")

        elif option == "5":
            manager.save_cafe(cafe_inv)
            print("Inventario terminado. Saliendo...")
            break
        else:
            print("Opción no válida.")
            input("Presione enter para intentar de nuevo...")