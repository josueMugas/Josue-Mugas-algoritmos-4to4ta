def recorrer():
    lista1=[]
    for x in range(1,6):
        numero=int(input(f"ingrese el nro{x}: "))
        lista1.append(numero)
    for numero in lista1:
        print(numero)

def busqueda():
        frutas=["pera","naranja","manzana","naranja","tomate"]
        fruta_buscar=input("ingrese una fruta: ")
        for fruta in frutas:
            indice=frutas.index(fruta)
            if fruta==fruta_buscar:
                print(f"la fruta esta en la posicion {indice}")
                break
        if fruta!=fruta_buscar:
            print("la fruta no se encuentra en la lista")
def notas():
    notas=[1,5,6,7,8,9,10,6,7,5,]
    suma=0
    for numero in notas:
        suma+=numero
    promedio=suma/10
    print(f"el promedio de notas es de {promedio}")
def temperaturas():
    temperaturas=[10,30,25,20,16,13,12]
    max=0
    min=1000
    promedio=0
    for temp in temperaturas:
        if temp>=max:
            max=temp
        if temp<=min:
            min=temp
        promedio+=temp
    promedio/=7
    print(f"la  temperatura maxima fue de: {max} la minima de: {min} y el promedio de: {promedio}")
def ordenar():
    numeros=[10,30,25,20,16,13,12,1,5,6,7,8,9,10,6,7,5,]
    numeros.sort()
    print(numeros)
def conteo():
    numeros=[10, 30, 25, 20, 16, 13, 12, 1, 5, 6, 7, 8, 9, 10, 6, 7, 5]
    pares=0
    impares=0
    for x in numeros:
        if x%2==0:
            pares+=1
        else:
            impares+=1
    print(f"la cantidad de pares={pares} impares={impares}")
