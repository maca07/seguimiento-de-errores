import math
datos1 = [160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503]
datos2 = [160, 591]
datos3 = [160, 591, 114, 229, 230]
datos4 = [160, 591, 114, 229, 230, 270, 128]


def menu():
    print()
    print("PROGRAMA PARA CALCULAR LA MEDIA Y LA DESVIACIÓN ESTANDAR")
    print()
    print("Seleccione la opción deseada...")
    print("1) Calcular promedio")
    print("2) Calcular desviación")
    print("3) Salir")


def obtenerPromedio(lista):
    suma = 0
    for dato in lista:
        suma += dato
    return suma / len(lista)


def desviacionEstandar(lista):
    n = len(lista)
    #promedio = obtenerPromedio(datos)
    promedio = obtenerPromedio(lista)
    varianza = 0
    for dato in lista:
        varianza += math.pow((dato - promedio), 2)
    return varianza / (n - 1)


def obtenerDesviacion(varianza, lista):
    if(varianza == 0):
        varianza = desviacionEstandar(lista)
        return math.sqrt(varianza)
    elif(varianza > 0):
        return math.sqrt(varianza)


def main():
    salir = False
    datos = []
    varianza = 0
    while not salir:
        opcion = -1
        menu()
        opcion = input()
        if(opcion == '1'):
            promedio = obtenerPromedio(datos1)
            print("El Promedio de la lista 'datos1' es: ", promedio)
            

            promedio = obtenerPromedio(datos2)
            print("El Promedio de la lista 'datos2' es: ", promedio)
            

            promedio = obtenerPromedio(datos3)
            print("El Promedio de la lista 'datos3' es: ", promedio)
            

            promedio = obtenerPromedio(datos4)
            print("El Promedio de la lista 'datos4' es: ", promedio)
            input("Enter para continuar...")

        elif(opcion == '2'):
            desviacion = obtenerDesviacion(varianza, datos1)
            print("El valor de Desviacion estandar en la lista 'datos1' es: ", desviacion)

            desviacion = obtenerDesviacion(varianza, datos2)
            print("El valor de Desviacion estandar en la lista 'datos2' es: ", desviacion)

            desviacion = obtenerDesviacion(varianza, datos3)
            print("El valor de Desviacion estandar en la lista 'datos3' es: ", desviacion)

            desviacion = obtenerDesviacion(varianza, datos4)
            print("El valor de Desviacion estandar en la lista 'datos4' es: ", desviacion)
            input("Enter para continuar...")
        elif(opcion == '3'):
            salir = True
        else:
            print("No existe opción")


main()
