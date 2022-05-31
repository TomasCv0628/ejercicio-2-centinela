
# Input

cod = int(input("Inserte el codigo: "))
nombre = input("Digite el nombre del estudiante: ")
print("***************************************")
if cod != 0:
    nota1 = float(input("Inserte el valor de la primera nota: "))
    print("***************************************")
    nota2 = float(input("Inserte el valor de la segunda nota: "))
    print("***************************************")
    nota3 = float(input("Inserte el valor de la tercera nota: "))
    print("***************************************")
else:
    print("***************************************")
    print("Fin de los datos de entrada")
    print("***************************************")

# Processing

reprobados = 0
while cod != 0:
    notafin=(nota1+nota2+nota3)/3
    print("El estudiante con codido " + str(cod) + ", cuyo nombre es " + nombre + " obtuvo una nota de " + str(notafin))
    if notafin <3:
        reprobados = reprobados + 1
    cod= int(input("Inserte el codigo: "))
    nombre = input("Digite el nombre del estudiante: ")
    if cod != 0:
        nota1 = float(input("Inserte el valor de la primera nota: "))
        print("***************************************")
        nota2 = float(input("Inserte el valor de la segunda nota: "))
        print("***************************************")
        nota3 = float(input("Inserte el valor de la tercera nota: "))
        print("***************************************")
    else:
        print("Fin de los datos de entrada")
print("El numero de reprobados es " + str(reprobados) )
