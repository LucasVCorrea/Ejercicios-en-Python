def elegir_idioma():
    idioma = input("Eliga el idioma (´E´ para Español, ´I´ para Inglés): ")
    devolver = ""
    if idioma == "E" or idioma == "e":
        devolver = "Español"
        print("Idioma: {}".format(devolver))
    elif idioma == "I" or idioma == "i":
        devolver = "English"
        print("Language: {}".format(devolver))
    else:
        print("No se ha detectado el idioma, Español por defecto.")
        devolver = "Español"
        print("Idioma: {}".format(devolver))
    return devolver


def operaciones(idioma):
    print("")
    if idioma == "Español":
        valor1 = int(input("Ingrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))
        print("Los valores elegidos son: [{} y {}]".format(valor1, valor2))
        suma = valor1 + valor2
        resta = valor1 - valor2
        multiplicacion = valor1 * valor2
        division = round(valor1 / valor2)
        division_real = float(valor1) / float(valor2)
        print("(+) Suma: {}\n(-) Resta: {}\n(*) Multiplicacion: {}\n(/) Division: {}\n(/f) Division Real: {}\n".format(
            suma, resta, multiplicacion, division, division_real))
        reintentar(idioma)
    else:
        value1 = int(input("Enter the first value: "))
        value2 = int(input("Enter the second value: "))
        print("Chosen values: [{} and {}]".format(value1, value2))
        addition = value1 + value2
        substraction = value1 - value2
        multiplication = value1 * value2
        division = round(value1 / value2)
        decimal_division = float(value1) / float(value2)
        print("(+) Addition: {}\n(-) Substraction: {}\n(*) Multiplication: {}\n(/) Division: {}\n(/f) Decimal division: {}\n".format(
            addition, substraction, multiplication, division, decimal_division))
        reintentar(idioma)
    return
def reintentar(idioma):
    if idioma=="Español":
        reintento=input("Quiere volver a ingresar? (s/n): ")
        while reintento !=0:
            if reintento=="s":
                operaciones(idioma)
            else:
                print("Hasta luego!")
            return
    else:
        try_again=input("Do you wanna try again? (y/n): ")
        while try_again!=0:
            if try_again=="y":
                operaciones(idioma)
            else:
                print("See you around!")
            return

def main():
    idioma = elegir_idioma()
    operaciones(idioma)
    return


main()
