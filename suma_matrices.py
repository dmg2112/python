import random 
import sys

dimMatriz = input("introduzca el numero de columnas en la matriz: ")
while(not dimMatriz.isdigit()):
    dimMatriz = input("introduzca un numero positivo: ")


dimMatriz= int(dimMatriz)
    
matriz = []
matrizBase = []
veces = 0
for i in range(dimMatriz):
    fila1 = []
    fila2 = []
    for j in range(dimMatriz):
        rng =random.randrange(1, 100,1)
        fila1.append(rng)
        fila2.append(rng)
    
    matrizBase.append(fila1)
    matriz.append(fila2)







total = 0

numero = input("introduzca el numero a rebasar: ")
while(not (numero.isdigit())):
    numero = input("introduzca un numero positivo: ")




numero= int(numero)

while ( total<numero):
    total = 0
    for i in range(dimMatriz):
        col1= matriz[i]
        col2 = matrizBase[i]
        for j in range(dimMatriz):
            col1[j] += col2[j]
    for x in matriz:
        for y in x:
            total+=y

    

    veces+=1


if(veces ==  1):
    print("el sumatorio solo ha requerido una vez")
else:
    print("numero de veces: "+ str(veces))





        
    
