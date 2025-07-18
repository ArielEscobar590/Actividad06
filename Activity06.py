try:

    productos = {}
    cantidad = int(input("\n¿Cuántos productos distintos hay en existencia? : "))
    for i in range(cantidad):
        print(f"\nProducto No.{i + 1}")
        while True:
            codigo = int(input("\nIngrese el Código del producto: "))
            if codigo in productos:
                print(f"\nProducto {codigo} ya existe, vuelve a intentarlo.")
            else:
                break

        nombre = input("\nIngrese el Nombre del producto: ")
        categoria = input("\nIngrese la Categoría del producto: ")
        talla = input("\nIngrese la Talla del producto: ")
        while True:
            preciouni = int(input("\nIngrese el Precio Unitario del producto: "))
            if preciouni <= 0:
                print("Error ha ingresado un precio unitario menor o igual a 0")
            else:
                break
        while True:
            stock = int(input("\nIngrese el Stock del producto: "))
            if stock <= 0:
                print("Error ha ingresado un stock menor a 0")
            else:
                break

        productos[codigo] = {
            "nombre": nombre,
            "categoria": categoria,
            "talla": talla,
            "preciouni": preciouni,
            "stock": stock,
        }
    a = 0
    print("\n")
    print("\nLista de Productos:")
    for codigo, datos in productos.items():
        print(f"\nProducto No.{a + 1}")
        print(f"Código del Producto: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Categoria: {datos['categoria']}")
        print(f"Talla: {datos['talla']}")
        print(f"Precio Unitario: {datos['preciouni']}")
        print(f"Stock: {datos['stock']}")
        print("\n")

    print("\nBuscar Producto")
    buscar = int(input("\nIngrese Código del Producto: "))
    if buscar in productos:
        print(f"Nombre: {productos[buscar]['nombre']}")
        print(f"Categoria: {productos[buscar]['categoria']}")
        print(f"Talla: {productos[buscar]['talla']}")
        print(f"Precio Unitario: {productos[buscar]['preciouni']}")
        print(f"Stock: {productos[buscar]['stock']}")

    else:
        print("Producto no Encontrado")

    woman = 0
    men = 0
    kids = 0
    for codigo, datos in productos.items():
        if datos['categoria'] == "Mujer":
            woman += 1
        elif datos['categoria'] == "Hombre":
            men += 1
        elif datos['categoria'] == "Niño":
            kids += 1

    print("\nRopa por categoria")
    print(f"Mujeres: {woman}")
    print(f"Hombres: {men}")
    print(f"Niño: {kids}")

    subtotal = 0
    total = 0
    for codigo, datos in productos.items():
        subtotal = datos['preciouni'] * datos['stock']
        total += subtotal

    print(f"\nValor total del Inventario: {total}")
except:
    print("Ha ocurrido un error")



