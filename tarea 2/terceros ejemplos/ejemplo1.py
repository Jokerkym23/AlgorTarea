def cargar():
    productos= ( )
    for x in range(5):
        nombre=input("ingresar el nombre del productos:")
        precio=int(input("ingrese el precio:"))
        productos[nombre]=precio
    return productos

def imprimir(productos):
    print("lista de todos los articulos")
    for nombre in productos:
        print(nombre, productos[nombre])

def imprimir_mayor100(productos):
    print("lista de articulos con precio mayores a 100")
    for nombre in productos:
        if productos[nombre]>100:
            print(nombre)

#bloque princicpal
productos=cargar()
imprimir(productos)
imprimir_mayor100(producto)
