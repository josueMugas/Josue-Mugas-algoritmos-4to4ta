import  random
def banco():

    try:
        saldo=1000
        while (True):
                print("""
                |====================|
                | 1) retirar         |
                | 2) depositar       |
                | 3) salir           |
                |====================|
                """)
                opcion= int(input("ingrese una opcion: "))
                if opcion==1:
                    retiro= int(input("ingrese el monto a retirar: "))
                    if retiro>saldo:
                        print("saldo insuficiente")
                    else:
                        saldo-=retiro
                        print(f" el saldo actual es de {saldo}")
                elif opcion==2:
                    ingreso=int(input("ingrese el monto a depositar: "))
                    saldo+=ingreso
                    print(f"su saldo actual es de {saldo}")
                elif opcion ==3:
                    print("saliendo...")
                    break
                else:
                    print("ingrse una opcion valida")
    except ValueError:
        saldo=1000
        print("ingrese un valor valido")
        while (True):
                print("""
                |====================|
                | 1) retirar         |
                | 2) depositar       |
                | 3) salir           |
                |====================|
                """)
                opcion= int(input("ingrese una opcion: "))
                if opcion==1:
                    retiro= int(input("ingrese el monto a retirar: "))
                    if retiro>saldo:
                        print("saldo insuficiente")
                    else:
                        saldo-=retiro
                        print(f" el saldo actual es de {saldo}")
                elif opcion==2:
                    ingreso=int(input("ingrese el monto a depositar: "))
                    saldo+=ingreso
                    print(f"su saldo actual es de {saldo}")
                elif opcion ==3:
                    print("saliendo...")
                    break
                else:
                    print("ingrse una opcion valida")

def IMC():
    try:
        altura=int(input("ingrese su altura: "))
        peso=int(input("ingrese su peso: "))
        IMC=peso/(peso**2)
        if IMC<17:
            print("estas muy flaco")
        elif IMC<=18.4:
            print("tas flaquito")
        elif IMC<25:
            print("tas joya")
        elif IMC<30:
            print("tas gordito")
        else:
            print("raja de aca hipopotamo")
    except (ZeroDivisionError, ValueError):
        print("ingrese valores validos")
        altura=int(input("ingrese su altura: "))
        peso=int(input("ingrese su peso: "))
        IMC=peso/(peso**2)
        if IMC<17:
            print("estas muy flaco")
        elif IMC<=18.4:
            print("tas flaquito")
        elif IMC<25:
            print("tas joya")
        elif IMC<30:
            print("tas gordito")
        else:
            print("raja de aca hipopotamo")

def AgustinFornite2008():
        vocales=["a","e","i","o","u"]
        palabra=""
        while palabra!="agustinfornite2008":
            palabra= input("ingrese una frase: ")

            for letra in range(len(palabra)-1):
                if palabra[letra] in vocales:
                    vocalesIndice=random.randint(0,4)
                    palabra=palabra.replace(palabra[letra],vocales[vocalesIndice])
            print(palabra)

def volteador():
    palabra=input("ingrese una palabra: ")
    palabrasSplit=palabra.split()
    palabraAlrevez=""
    for substring in palabrasSplit:
        palabraAlrevez += " "+substring[::-1]
    print(palabraAlrevez)


def alumnos():
    Lista_Nombres = []
    Seguimos = True

    while Seguimos:
        try:
            Ingreso_Usuario = int(input("""

                1. Ingresar alumno en lista
                2. Ver Alumno
                3. Salir
            """))
            if Ingreso_Usuario == 1:
                Nombre_a_Ingresar = input("Ingrese un nombre")
                Lista_Nombres.append(Nombre_a_Ingresar)
                Seguimos = True
            elif Ingreso_Usuario == 2:
                print("Lista de Alumnos", Lista_Nombres)
                Ver_Alumno = int(input("Ingrese indice de alumno"))
                print(Lista_Nombres[Ver_Alumno - 1])
                Seguimos = True
            elif Ingreso_Usuario == 3:
                print("chau")
                Seguimos = False
        except ValueError:
            print("Tipo de dato ingresado incorrecto")
        except IndexError:
            print("Indice de la lista no disponible")