def diviciones():
    a=int(input("ingrese el dividendo: "))
    b=int(input("ingrese el divisor: "))
    try:
       resultado = a/b
       print(f"el resultado es de {resultado}")
    except ZeroDivisionError:
       print("Error: No puedes dividir por cero.")
    finally:
        print("termino la divicion")

def VerificadorTexto():
    x=True
    while x:
        try:
            edad = int(input("ingrese su edad: "))
            x = False
        except ValueError:

                print("ingrese valores validos")
        if x==False:
                print(edad)
def ListaNombres():
    lista=["pedro","ana","sofia"]
    indice=int(input("ingrese el indice del nombre a buscar"))
    try:
        print(f"el nombre es {lista[indice]}")
    except IndexError:
        print("el indice no fue encontrado")
    finally:
        print("chao")
def convertorNumeros():
    try:
        numero1=input("ingrese un numero: ")
        numero2=input("ingrese otro numero: ")
        numero1=int(numero1)
        numero2=int(numero2)
        suma=numero1+numero2
        print(f"el resultado es {suma}")
    except ValueError:
        print("los datos dados no son correctos")
    except TypeError:
        print("se intento sumar un entero con texto")
def calculo():

    try:
        a = int(input("ingrese el dividendo: "))
        b = int(input("ingrese el divisor: "))
        resultado = a / b
        print(f"el resultado es de {resultado}")
    except (ZeroDivisionError,ValueError):
        print("Error: valores invalidos.")
    finally:
        print( "Fin del programa de cálculo")
ListaNombres()