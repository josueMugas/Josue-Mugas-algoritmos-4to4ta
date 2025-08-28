def mostrar():
    matriz=[[1,2,3],
            [4,5,6],
            [7,8,9]]
    for x in matriz:
        print(x)

def suma_todo():
    matriz=[[10,20,30],[40,50,60],[70,80,90]]
    suma=0
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            suma+=matriz[x][y]
    print(suma)


def buscarXindice():
    matriz = [
        [25, 10, 4, 17],
        [3, 22, 14, 8],
        [19, 28, 6, 12],
        [20, 5, 26, 9]
    ]
    indiceX=int(input("ingrese la posicion en x del elemento: "))
    indiceY=int(input("ingrese la posicion en y del elemento: "))
    print(matriz[indiceX-1][indiceY-1])

def masGrande():
    mas_grande = 0
    matriz = [
        [25, 10, 4, 17],
        [3, 22, 14, 8],
        [19, 28, 6, 12],
        [20, 5, 26, 9]
    ]
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if matriz[x][y] > mas_grande:
                contador = matriz[x][y]
    print(mas_grande)
masGrande()