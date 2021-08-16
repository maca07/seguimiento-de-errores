import math
datos1 = []
datos2 = [160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503]
datos3 = [15.0,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]


def agregardatos(numero):
    for i in range(int(numero)):
        print("Ingrese numero" )
        agregar=input()
        datos1.append(int(agregar))

def menu():
    print()
    print("PROGRAMA PARA CALCULAR LA MEDIA Y LA DESVIACIÓN ESTANDAR")
    print()
    print("Seleccione la opción deseada...")
    print("1) Ingresar datos por Teclado")
    print("2) Calcular media y desviacíon con un arreglo lleno ejemplo 1 ")
    print("3) Calcular media y desviacíon con un arreglo lleno ejemplo 2 ")
    print("4) Salir")


def obtenerPromedio(lista):
    suma = 0
    for dato in lista:
        suma += dato
        
    return suma/ len(lista)

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


#def luego():
 #    promedio = obtenerPromedio(datos1)
            
    #print("El Promedio de la lista 'datos1' es: ", promedio
    #promedio = obtenerPromedio(datos2)
    #print("El Promedio de la lista 'datos2' es: ", promedio)
    
    #promedio = obtenerPromedio(datos3)
    #print("El Promedio de la lista 'datos3' es: ", promedio)

def main():
    salir = False
    datos = []
    varianza = 0
    while not salir:
        opcion = -1
        menu()
        opcion = input()
        if(opcion == '1'):
            print ("ingresa el numero de datos en la lista")
            numero = input()
            agregardatos(numero)
            promedio = obtenerPromedio(datos1)
            print("El Promedio de la lista 'datos4' es: ", promedio)
            desviacion = obtenerDesviacion(varianza, datos1)
            print("El valor de Desviacion estandar en la lista 'datos1' es: ", desviacion)
            input("Enter para continuar...")

        elif(opcion == '2'):

            promedio = obtenerPromedio(datos2)
            print("El Promedio de la lista 'datos2' es: ", promedio)
            desviacion = obtenerDesviacion(varianza, datos2)
            print("El valor de Desviacion estandar en la lista 'datos2' es: ", desviacion)
            input("Enter para continuar...")

        elif(opcion == '3'):
    
            promedio = obtenerPromedio(datos2)
            print("El Promedio de la lista 'datos3' es: ", promedio)
            desviacion = obtenerDesviacion(varianza, datos2)
            print("El valor de Desviacion estandar en la lista 'datos2' es: ", desviacion)
            input("Enter para continuar...")


            
            input("Enter para continuar...")
        elif(opcion == '4'):
            salir = True
        else:
            print("No existe opción")

main()