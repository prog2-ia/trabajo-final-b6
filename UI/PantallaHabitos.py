from entidades import *
from persistencia import *
from servicios import *

def menu():
    opcion =-1
    while opcion < 1 or opcion > 1:
        print('===MENU==')
        print('1. Crear hábito')
        opcion= int(input("Introduce una opción: "))
        if opcion==1:
            return



menu()