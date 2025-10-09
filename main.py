productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 25, "categoria": "Electrónica"},
    {"nombre": "Teclado", "precio": 75, "categoria": "Electrónica"},
    {"nombre": "Silla de Oficina", "precio": 300, "categoria": "Muebles"}]

def recorrerDiccionario():
    for producto in productos:
        print(producto["nombre"])

def sumaTotal():
    suma=0
    for producto in productos:
        suma+=producto["precio"]
    print(f"la suma total de los precios es de {suma}")

def añadirProducto():
    nombre=input("ingrese el nombre del producto a añadir: ")
    precio=int(input("Ingrese el precio del producto:"))
    categoria=input("Ingrese la categoria del producto")
    producto={"nombre":nombre,"precio":precio,"categoria":categoria}
    productos.append(producto)
def actualizacionPrecio():
    indice=int(input("ingrese la pocicion del producto al que desea cambiar el precio: "))
    NuevoPrecio=int(input("ingrese el nuevo precio: "))
    productos[indice]["precio"]=NuevoPrecio
    print(productos[indice])
estudiantes = [
    {"nombre": "Ana", "edad": 21, "calificacion": 90},
    {"nombre": "Luis", "edad": 22, "calificacion": 95},
    {"nombre": "Marta", "edad": 20, "calificacion": 85}
]
def BusquedaMasGrande():
    MasGrande=0
    for estudiante in estudiantes:
        if estudiante["calificacion"]>MasGrande:
            MasGrande=estudiante["calificacion"]
            mejor=estudiante
    print(f"el estudiante con mas nota fue {mejor}")

def CrearLista():
    NombresEstudiantes=[]
    for estudiante in estudiantes:
        NombresEstudiantes.append(estudiante["nombre"])
    print(NombresEstudiantes)

libros = [
    {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
    {"titulo": "Don Quijote", "autor": "Miguel de Cervantes"},
    {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"}
]
def AñadirQuitar():
    libro=libros[1]
    print(libros)
    libros.pop(1)
    print(libros)
    libros.append(libro)
    print(libros)

def AñadirDisponibilidad():
    for libro in libros:
        libro["disponible"]=True
        print(libro)