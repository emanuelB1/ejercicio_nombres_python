lista_nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]



def hacer_grandioso(lista):
    lista_magos = []
    lista_cientificos = []
    lista_otros = []
    lista_magos_grandiosos = []
    for nombre in lista:
        if nombre == "Harry Houdini":
            lista_magos.append(nombre)
        elif nombre == "David Blaine":
            lista_magos.append(nombre)
        elif nombre == "Teller":
            lista_magos.append(nombre)
        elif nombre == "Newton":
            lista_cientificos.append(nombre)
        elif nombre == "Hawking":
            lista_cientificos.append(nombre)
        elif nombre == "Einstein":
            lista_cientificos.append(nombre)
        else:
            lista_otros.append(nombre)
    for mago in lista_magos:
        mago = "El gran " + mago
        lista_magos_grandiosos.append(mago)
    print("*" * 17 + " Magos Grandiosos " + "*" * 17)
    for mago in lista_magos_grandiosos:
        print(mago)
    print("*" * 19 + " Cientificos " + "*" * 20)
    for cientifico in lista_cientificos:
        print(cientifico)
    print("*" * 17 + " Otros Personajes " + "*" * 17)
    for personaje in lista_otros:
        print(personaje)
    print("*" * 17 + " Todas las Listas " + "*" * 17)
    print("Lista de Magos:", lista_magos)
    print("Lista de los Grandes Magos:", lista_magos_grandiosos)
    print("Lista de los Cientificos:", lista_cientificos)
    print("Lista de otros Personajes:", lista_otros)

def imprimir_nombres(lista):
    print("*" * 16 + " Todos los Nombres " + "*" * 16)
    for nombre in lista:
        print(nombre)
    hacer_grandioso(lista)
    print("Lista de Todos los Nombres:", lista)



imprimir_nombres(lista_nombres)   
    
     
           
