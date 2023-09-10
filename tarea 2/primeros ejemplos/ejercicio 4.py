#realice la carga de valores enteros por teclado
#almacenarlos en una lista. finalizar la carga de enteros al ingresa el cero
#mostrar finalmente el tamaño de la lista
lista=[]
valor=int(input ("ingrese valor (0 para finalizar):"))
while valor!=0:
        lista.append(valor)
        valor=int(input("ingresar valor (0para finalizar):"))

print("tamaño de la lista:")
print (len(lista))
