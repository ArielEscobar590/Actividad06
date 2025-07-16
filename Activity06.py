productos={}
cantidad=int(input("\n¿Cuántos productos distintos hay en existencia? : "))
for i in range(cantidad):
    print(f"\nProducto No.{i+1}")
    while True:
        codigo = int(input("\nIngrese el Código del producto: "))
        if codigo in productos:
            print(f"\nProducto {codigo} ya existe, vuelve a intentarlo.")
        else:
            break

    nombre=input("\nIngrese el Nombre del producto: ")
    categoria=input("\nIngrese la Categoría del producto: ")
    talla=input("\nIngrese la Talla del producto: ")
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

woman= 0
men = 0
kids= 0
for codigo,datos in productos.items():
    if datos['Categoria'] <= "Mujer":
        woman+=1
    elif datos['Categoria'] <= "Hombre":
        men+=1
    elif datos['Categoria'] <= "Niño":
        kids+=1

print("\nRopa por categoria")
print(f"\nMujeres: {woman}")
print(f"\nHombres: {men}")
print(f"\nNiño: {kids}")

subtotal = 0
totaluni = 0
total = 0
cantidad = 0
for codigo,datos in productos.items():
    subtotal = datos['preciouni'] * datos['stock']
    total += subtotal

print(total)




