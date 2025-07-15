productos={}
cantidad=int(input("\n¿Cuántos productos distintos hay en existencia? : "))
for i in range(cantidad):
    print(f"\nProducto No.{i+1}")
    codigo= int(input("\nIngrese el Código del producto: "))
    nombre=input("\nIngrese el Código del producto: ")
    categoria=input("\nIngrese el Código del producto: ")
    talla=input("\nIngrese el Código del producto: ")
    preciouni = int(input("\nIngrese el Código del producto: "))
    stock = int(input("\nIngrese el Código del producto: "))
    productos[codigo]={
        "nombre":nombre,
        "categoría":categoria,
        "talla":talla,
        "preciouni":preciouni,
        "stock":stock,
    }
a = 0
print("\nLista de Productos:")
for codigo,datos in productos.items():
    print("\n")
    print(f"\nProducto No.{a+1}")
    print(f"\nCódigo del Producto: {codigo}")
    print(f"\nNombre: {datos['nombre']}")
    print(f"\nCategoria: {datos['categoria']}")
    print(f"\nTalla: {datos['talla']}")
    print(f"\nPrecio Unitario: {datos['preciouni']}")
    print(f"\nStock: {datos['stock']}")
    print("\n")

print("\nBuscar Producto")
buscar=input("\nIngrese Código del Producto: ")
if buscar in productos:
    print(f"\nNombre: {productos[buscar]['nombre']}")
    print(f"\nCategoria: {productos[buscar]['categoria']}")
    print(f"\nTalla: {productos[buscar]['talla']}")
    print(f"\nPrecio Unitario: {productos[buscar]['preciouni']}")
    print(f"\nStock: {productos[buscar]['stock']}")

else:
    print("Producto no Encontrado")


