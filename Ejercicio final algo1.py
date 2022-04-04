maximo = "99999"


def leer(archivo):
    linea_entera = archivo.readline()
    if linea_entera:
        linea_separada = linea_entera.rstrip("\n").split(",")
    else:
        linea_separada = maximo, ""
    return linea_separada


def generar_archivo(archivo_a_generar, fecha, sucursal, cant_total_sucurs):
    archivo_a_generar.write(fecha + "," + sucursal + "," + str(cant_total_sucurs) + "\n")
    return


def generar_diccionario(diccionario, codigo_sucursal):
    if codigo_sucursal not in diccionario:
        diccionario[codigo_sucursal] = 1
    else:
        diccionario[codigo_sucursal] += 1
    return


def mezclar_archivos(archivo_avella, archivo_lomas, archivo_temper, archivo_unificado_sucursales):
    fecha_avella, ISBN_avella = leer(archivo_avella)
    fecha_lomas, ISBN_lomas = leer(archivo_lomas)
    fecha_temperl, ISBN_temperl = leer(archivo_temper)
    ventas_generales = 0
    diccionario_codigos = {}
    while fecha_avella != maximo or fecha_lomas != maximo or fecha_temperl != maximo:
        menor_fecha = min(fecha_avella, fecha_lomas, fecha_temperl)
        total_vtas_por_fecha = 0
        print("Fecha: {}".format(menor_fecha))
        while fecha_avella != maximo and fecha_avella == menor_fecha:
            sucursal_anterior = "Avellaneda"
            total_vtas_por_sucursal = 0
            while fecha_avella != maximo and fecha_avella == menor_fecha and sucursal_anterior == "Avellaneda":
                total_vtas_por_sucursal += 1
                total_vtas_por_fecha += 1
                generar_diccionario(diccionario_codigos, ISBN_avella)
                print(" {} ({})".format(ISBN_avella, sucursal_anterior))
                fecha_avella, ISBN_avella = leer(archivo_avella)
            generar_archivo(archivo_unificado_sucursales, menor_fecha, sucursal_anterior, total_vtas_por_sucursal)
            print(" -Total de {}: {} libros vendidos-".format(sucursal_anterior.upper(), total_vtas_por_sucursal))

        while fecha_lomas != maximo and fecha_lomas == menor_fecha:
            sucursal_anterior = "Lomas"
            total_vtas_por_sucursal = 0
            while fecha_lomas != maximo and fecha_lomas == menor_fecha and sucursal_anterior == "Lomas":
                total_vtas_por_sucursal += 1
                total_vtas_por_fecha += 1
                generar_diccionario(diccionario_codigos, ISBN_lomas)
                print(" {} ({})".format(ISBN_lomas, sucursal_anterior))
                fecha_lomas, ISBN_lomas = leer(archivo_lomas)
            generar_archivo(archivo_unificado_sucursales, menor_fecha, sucursal_anterior, total_vtas_por_sucursal)
            print(" -Total de {}: {} libros vendidos-".format(sucursal_anterior.upper(), total_vtas_por_sucursal))
        while fecha_temperl != maximo and fecha_temperl == menor_fecha:
            sucursal_anterior = "Temperley"
            total_vtas_por_sucursal = 0
            while fecha_temperl != maximo and fecha_temperl == menor_fecha and sucursal_anterior == "Temperley":
                total_vtas_por_sucursal += 1
                total_vtas_por_fecha += 1
                generar_diccionario(diccionario_codigos, ISBN_temperl)
                print(" {} ({})".format(ISBN_temperl, sucursal_anterior))
                fecha_temperl, ISBN_temperl = leer(archivo_temper)
            generar_archivo(archivo_unificado_sucursales, menor_fecha, sucursal_anterior, total_vtas_por_sucursal)
            print(" -Total de {}: {} libros vendidos-".format(sucursal_anterior.upper(), total_vtas_por_sucursal))
        ventas_generales += total_vtas_por_fecha
        print("[Total de la fecha: {} libros vendidos]\n".format(total_vtas_por_fecha))
    print("//El total general es de: {} libros vendidos//\n".format(ventas_generales))
    return diccionario_codigos


def armar_ranking_codigos(diccionario_codigos):
    diccionario_ordenado = sorted(diccionario_codigos.items(), key=lambda x: x[1], reverse=True)
    print("Ranking de las ventas: ")
    for codigo in diccionario_ordenado:
        nombre_codigo = 0
        cantidad = 1
        print("{} - {} libro/s vendido/s".format(codigo[nombre_codigo], codigo[cantidad]))
    return


def main():
    archivo_vtas_avella = open("VTAS_Avellaneda.csv", "r")
    archivo_vtas_lomas = open("VTAS_Lomas.csv", "r")
    archivo_vtas_temper = open("VTAS_Temperley.csv", "r")
    archivo_vtas_unificado = open("VENTAS.CSV", "w")
    diccionario = mezclar_archivos(archivo_vtas_avella, archivo_vtas_lomas, archivo_vtas_temper, archivo_vtas_unificado)
    armar_ranking_codigos(diccionario)
    archivo_vtas_avella.close()
    archivo_vtas_lomas.close()
    archivo_vtas_temper.close()
    archivo_vtas_unificado.close()
    return


main()
