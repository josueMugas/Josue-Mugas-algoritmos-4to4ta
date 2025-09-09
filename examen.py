import random

def crearMazo():
    posiblesPalos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    mazo = []
    for palo in posiblesPalos:
            for numero in range(1, 14):
                if numero==1:
                    carta = ["A", palo]
                elif numero==11:
                    carta = ["J", palo]
                elif numero==12:
                    carta = ["Q", palo]
                elif numero==13:
                    carta = ["K", palo]
                else:
                    carta=[numero, palo]
                mazo.append(carta)
    return mazo

def crearMano():
    mano = []
    global mazo
    for carta in range(8):
        indice = random.randint(0, len(mazo) - 1)
        mano.append(mazo[indice])
        mazo.pop(indice)
    return mano

def descartar_carta():
    global mano, mazo
    print("Tu mano:", mano)
    try:
        descartado=[]
        indice = int(input("Ingrese la posición de la carta que desea descartar (1-5): "))
        if 1 <= indice <= len(mano):
            carta_descartada = mano.pop(indice - 1)
            print(f"Descartaste: {carta_descartada}")
            if len(mazo) > 0:
                nueva_carta = mazo.pop(random.randint(0, len(mazo) - 1))
                mano.append(nueva_carta)
                print(f"Tu nueva carta es: {nueva_carta}")
            else:
                print("El mazo está vacío, no se puede reponer carta.")
            descartado.append(carta_descartada)

        else:
            print("Posición inválida.")
    except ValueError:
        print("Por favor ingrese un número válido.")
def jugar():
    global mano,mazo
    chips_totales=0
    if mazo!=[]:
        for carta in mano:
            if carta[0]=="A":
                chips_totales+=11
            elif carta[0]=="J" or carta[0]=="Q" or carta[0]=="K":
                chips_totales+=10
            else:
                chips_totales+=carta[0]
            mano.remove(carta)
            nueva_carta = mazo.pop(random.randint(0, len(mazo) - 1))
            mano.append(nueva_carta)
        return chips_totales
    else:
        print("mazo vacio")
        for carta in mano:
            if carta[0]=="A":
                chips_totales+=11
            elif carta[0]=="J" or carta[0]=="Q" or carta[0]=="K":
                chips_totales+=10
            else:
                chips_totales+=carta[0]
            mano.remove(carta)
        return chips_totales
mazo = crearMazo()
mano = crearMano()
while len(mano)>0:
    try:
        print(mano)
        opcion = int(input("""
              |====================|
              |        menu        |
              |                    |
              |1) mostrar mazo     |
              |                    |
              |2) descartar        |
              |                    |
              |3)jugar             |
              |                    |   
              |4) salir            |
              |                    |
              |====================|
              
              ingrese una opcion: """
              ))
        if opcion == 1:
            print("El mazo es: ")
            for carta in mazo:
                print(carta)
        elif opcion == 2:
            descartar_carta()
        elif opcion ==3:
            chips=jugar()
            print(f"la puntuacion es de: {chips}")
            if len(mano)!=0:
                print("la nueva mano es: ")
            else:
                print("no hay mas cartas.")

        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Poné una opción válida.")
    except ValueError:
        print("Ingrese una opción válida.")