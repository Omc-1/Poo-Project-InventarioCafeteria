import Productos

Productos.agregar_producto()
def mostrar_menu():
    print("\n--- MENÚ DE NIEVES ---")
    print("1. Nieve de chocolate ($30)")
    print("2. Nieve de vainilla ($25)")
    print("3. Nieve de fresa ($28)")
    print("4. vaso ($5)")
    print("5. cono($10")
    print("6. Salir")
    print("7. Inventario")

total = 0

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        total += 30
        print("✔ Agregaste nieve de chocolate 🍫")
    elif opcion == "2":
        total += 25
        print("✔ Agregaste nieve de vainilla 🍦")
    elif opcion == "3":
        total += 28
        print("✔ Agregaste nieve de fresa 🍓")
    elif opcion == "4":
        total += 5
        print("✔ agregaste el vaso")
    elif opcion == "5":
        total += 10
        print("✔ agregaste el cono")
    elif opcion == "6":
        print("\nSaliendo del sistema...")

    elif opcion == "7":
        print("Ingresando al inventario")
        break
    else:
        print("❌ Opción inválida, intente de nuevo.")

    print(f"💰 Total actual: ${total}")

print(f"\n🧾 Total a pagar: ${total}")

if total > 0:
    print("Gracias por su compra 😊")

while True:
    print("\n1. Agregar ingrediente")
    print("2. Ver inventario")
    print("3. Ver productos por caducar")
    print("4. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        productos_por_caducar()
    elif opcion == "4":
        break
