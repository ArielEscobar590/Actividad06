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


