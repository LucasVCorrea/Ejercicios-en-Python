numero = input("Ingrese el numero binario: ")
contador = len(numero)
sumatoria = 0
for numeritos in numero:
    contador -= 1
    sumatoria += int(numeritos)*(2** contador)
    print("{} x 2**{}".format(numeritos,contador))
print("El numero {} = {} en decimal".format(numero,sumatoria))
