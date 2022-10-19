from config import *
from votacion import *
import tkinter as tk
from tkinter import ttk
import string
import random


def main():
    '''Inicializa el programa. Formatea resultados_parciales.txt. Inicia ventana de Bloqueo'''
    candidatos = []  # lista de candidatos
    contras = []  # lista de contraseñas generadas

    # formatear el txt
    with open("resultados_parciales.txt", mode="r+") as f:
        f.write("elegido: \nprimera vez")
        f.seek(0)

    # iniciar la ventana de bloqueo
    bloqueo(contras, candidatos)


def generador_contra():
    '''
    Devuelve una contraseña aleatoria de 8 letras.

        Returns:
            contra_generada (str): contraseña generada. 8 letras aleatorias
    '''
    # se guardan todas las letras del alfabeto
    letras = string.ascii_lowercase
    # se eligen 8 letras al azar y se devuelve como contraseña
    contra_generada = ''.join(random.choice(letras) for i in range(8))
    return contra_generada


def bloqueo(contras, candidatos):
    '''
    Pantalla inicial y la más usada. Bloquea la votacion hasta que se ingrese una de las contraseñas

        Parameters:
            contras (list): lista de las contraseñas
            condidatos (list): lista de los candidatos
    '''
    contra_votantes = ["contraseña", "contraseña2"]

    Bloqueo = tk.Tk()
    window_width = 600
    window_height = 600

    # Centrar Ventana
    # conseguir dimensiones de la pantalla
    screen_width = Bloqueo.winfo_screenwidth()
    screen_height = Bloqueo.winfo_screenheight()
    # hallar el centro
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # poner posicion de ventana en el centro de la pantalla
    Bloqueo.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Configuracion de la grid
    Bloqueo.columnconfigure(0, weight=1)
    Bloqueo.columnconfigure(1, weight=3)

    Bloqueo.title("Sistema de Votación Automatizado")

    ttk.Label(Bloqueo, text="Ingresar Contraseña Personal:").grid(
        column=0, row=0, padx=5, pady=5, sticky=tk.E)

    contra = tk.StringVar()
    ttk.Entry(Bloqueo, textvariable=contra, show="*").grid(column=1, row=0, padx=5, pady=5, sticky=tk.EW)

    def chequear_contra():
        '''Chequea la contraseña ingresada y abre la ventana correspondiente.'''
        contra_ingresada = contra.get()
        contra.set("")
        if contra_ingresada == "admin":
            Bloqueo.destroy()
            print("contraseña config")
            config()

        elif contra_ingresada == "resultados":
            print("contraseña resultados")
        else:
            for i in range(len(contra_votantes)):
                if contra_ingresada == contras[i]:
                    print("contraseña correcta")
                    contras.remove(contra_ingresada)
                    print(contras)
                    votacion(candidatos)
                else:
                    print("contraseña equivocada")
    ttk.Button(Bloqueo, text="aceptar", command=chequear_contra).grid(
        column=1, row=1, padx=5, pady=5, sticky=tk.E)

    Bloqueo.mainloop()


if __name__ == '__main__':
    main()
