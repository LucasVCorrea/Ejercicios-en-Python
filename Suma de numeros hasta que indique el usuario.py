def pregunta():
    lista = []
    ingreso = int(input("Ingrese el numero a sumar, (ingrese 0 para terminar la suma): "))
    while ingreso != 0:
        lista.append(ingreso)
        ingreso = int(input("Ingrese el numero a sumar, (ingrese 0 para terminar la suma): "))
    return lista


def sumar_numeros(lista):
    # elementos_sumados=sum(lista)
    sumatoria = 0
    for numero in lista:
        sumatoria += numero
    print("{}= {}".format(lista,sumatoria) )
    lista=lista.clear()

def main():
    constante=True
    while constante:
        lista = pregunta()
        sumar_numeros(lista)
        final=input("Desea seguir ingresando? (s/n): ")
        if final=="n":
            print("Adios!")
            return

main()
