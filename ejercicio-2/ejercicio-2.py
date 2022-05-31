
n = int(input("Inserte un numero entero: "))

par = 0
impar = 0

while n != 0:
    r = n % 2
    if r == 0:
        par = par + 1
    else:
        impar = impar + 1
    n = int(input("Inserte un numero entero: "))
print("la cantidad de numeros impares es: " + str(impar) + ", la cantidad de numeros pares es:" + str(par))
