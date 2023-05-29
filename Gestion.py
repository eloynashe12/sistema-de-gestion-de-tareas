from Listas import *

def mostrar_menu(opciones):
    print('Seleccione una tarea:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Asignadas ', accion1),
        '2': ('Pendientes', accion2),
        '3': ('Terminada ', accion3),
        '4': ('Agregar tarea',accion4),
        '5': ('Salir', accion5)
    }

    generar_menu(opciones, '4')


def accion1():
    print('matematicas (2) , lenguaje(1) , ingles(1), salir(exit)')
    
    

def accion2():
    print('matematicas (1), lenguaje(0), ingles(1), salir(exit)')


def accion3():
    print('matematicas(1), lenguaje(1), ingles(0), salir(exit)')

def accion4():
    print('drive, word, ppt')

def accion5():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()