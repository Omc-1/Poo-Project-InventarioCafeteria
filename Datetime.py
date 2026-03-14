inventario = []


def agregar_producto():
    nombre = input("Nombre del ingrediente: ")
    cantidad = int(input("Cantidad en almacén: "))
    fecha = input("Fecha de caducidad (YYYY-MM-DD): ")

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "caducidad": fecha
    }

    inventario.append(producto)
    print("Producto agregado al inventario ✅")


def mostrar_inventario():
    print("\n--- INVENTARIO ---")
    for p in inventario:
        print(f"{p['nombre']} | Cantidad: {p['cantidad']} | Caduca: {p['caducidad']}")


def productos_por_caducar():
    hoy = datetime.now()
    print("\n--- POR CADUCAR ---")

    for p in inventario:
        fecha = datetime.strptime(p["caducidad"], "%Y-%m-%d")
        dias = (fecha - hoy).days

        if dias <= 7:
            print(f"{p['nombre']} caduca en {dias} días ⚠️")
