def armar_matriz(matriz):

    for i in range(0,len(matriz)):
        print("FILA {}".format(i+1))
        for j in range(0,len(matriz)):
            ingreso = int(input("Ingrese el valor {}: ".format(j + 1)))
            matriz[i].append(ingreso)

    for fila in range(0,len(matriz)):
        print(matriz[fila])

    return matriz

def sumar_matrices(matriz_1,matriz_2):
    pregunta = input("Suma o resta? ( + / - ): ")


    for i in range(0,len(matriz_1)):
        for j in range(0,len(matriz_1)):
            if pregunta == '+':
                matriz_1[i][j]+=matriz_2[i][j]
            elif pregunta == '-':
                matriz_1[i][j] -= matriz_2[i][j]
    return matriz_1

def imprimir_resultado(matriz_final):
    for fila in range(0,len(matriz_final)):
        print(matriz_final[fila])

def main():
    matriz = [[], [], []]
    matriz_2 = [[], [], []]
    print('\n',"Ingrese la primer matriz: ")
    mat_1=armar_matriz(matriz)
    print('\n',"Ingrese la segunda matriz: ")
    mat_2=armar_matriz(matriz_2)
    print('\n', "Resultado: ")
    matrix_final = sumar_matrices(mat_1,mat_2)
    imprimir_resultado(matrix_final)
main()
