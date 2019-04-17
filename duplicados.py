longi = input("introduzca el numero de elementos en la lista: ")
while(not (longi.isdigit())):
    longi = input("introduzca un numero positivo: ")

longi= int(longi)
eltos = []
for i in range(longi):
    elto = input("introduzca un elemento: ")
    if (elto.isdigit()):
        elto = int(elto)
    eltos.append(elto)

print("con duplicados:")
for elto in eltos:
    print(elto)
eltos = list(set(eltos))

print("sin duplicados y ordenado")
for elto in eltos:
    print(elto)

    





