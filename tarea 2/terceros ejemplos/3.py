def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("ingrese palbra en castellano:")
        ing=input("ingrese palabra en ingles:")
        diccionario[ing]=caste
        continua=input("quiere cargar otra palbra:[s/n]")
    return diccionario

def imprimir (diccionario):
    print("listado completo del diccionario")
    for ingles in diccionario:
        print(ingles,diccionario,[ingles])

def consulta_palbra(diccionario):
    pal=input("ingrese la palabra en ingles a consultar:")
    if pal in diccionario:
        print("en castellano significa",diccionario[pal])

diccionario=cargar()
imprimir[diccionario]
consulta_palbra(diccionario)