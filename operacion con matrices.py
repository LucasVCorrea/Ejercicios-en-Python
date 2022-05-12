def armar_matriz(matriz,filas,columnas):

    for i in range(0,filas):
        print("FILA {}".format(i+1))
        for j in range(0,columnas):
            ingreso = int(input("Ingrese el valor {}: ".format(j + 1)))
            matriz[i].append(ingreso)

    for fila in range(0,len(matriz)):
        print(matriz[fila])

    return matriz

def sumar_matrices(filas, columnas,matriz_1,matriz_2):

    pregunta = input("Suma o resta? ( + / - ): ")


    for i in range(0,filas):
        for j in range(0,columnas):
            if pregunta == '+':
                matriz_1[i][j]+=matriz_2[i][j]
            elif pregunta == '-':
                matriz_1[i][j] -= matriz_2[i][j]
    return matriz_1

def imprimir_resultado(matriz_final):
    for fila in range(0,len(matriz_final)):
        print(matriz_final[fila])

def definir_dimensiones(matriz1,matriz2):
    filas = int(input("Ingrese la cantidad de filas que va a tener la matriz: "))
    for i in range(0,filas):
        matriz1.append([])
        matriz2.append([])
    columnas = int(input("Ingrese la cantidad de columnas que va a tener la matriz: "))
    return filas,columnas
def main():
    matriz = []
    matriz_2 = []
    filas,columnas=definir_dimensiones(matriz,matriz_2)
    print('\n',"Ingrese la primer matriz: ")
    mat_1=armar_matriz(matriz,filas,columnas)
    print('\n',"Ingrese la segunda matriz: ")
    mat_2=armar_matriz(matriz_2,filas,columnas)
    print('\n', "Resultado: ")
    matrix_final = sumar_matrices(filas,columnas,mat_1,mat_2)
    imprimir_resultado(matrix_final)
main()