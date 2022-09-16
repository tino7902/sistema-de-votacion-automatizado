from config import *
from votacion import *
import tkinter as tk
from tkinter import ttk
import string
import random

def main():
    candidatos = []
    contras = []
    bloqueo(contras, candidatos)
    # config()

def generador_contra():
    letras = string.ascii_lowercase
    contra_generada = ''.join(random.choice(letras) for i in range(8))
    return contra_generada

def bloqueo(contras, candidatos):
    contra_votantes = ["contraseña", "contraseña2"]

    Bloqueo = tk.Tk()
    window_width = 600
    window_height = 600

    #Centrar Ventana
    ## conseguir dimensiones de la pantalla
    screen_width = Bloqueo.winfo_screenwidth()
    screen_height = Bloqueo.winfo_screenheight()
    # hallar el centro
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    # poner posicion de ventana en el centro de la pantalla
    Bloqueo.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    #Configuracion de la grid
    Bloqueo.columnconfigure(0, weight=1)
    Bloqueo.columnconfigure(1, weight=3)

    Bloqueo.title("Sistema de Votación Automatizado")

    ttk.Label(Bloqueo, text="Ingresar Contraseña Personal:").grid(column=0, row=0, padx=5, pady=5, sticky=tk.E)

    contra = tk.StringVar()
    ttk.Entry(Bloqueo, textvariable=contra, show="*").grid(column=1, row=0, padx=5, pady=5, sticky=tk.EW)

    def chequear_contra():
        contra_ingresada =contra.get()
        if contra_ingresada == "12345678":
            Bloqueo.destroy()
            print("contraseña config")
            config()
            
        elif contra_ingresada == "87654321":
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
    ttk.Button(Bloqueo, text="aceptar", command=chequear_contra).grid(column=1, row=1, padx=5, pady=5, sticky=tk.E)

    Bloqueo.mainloop()


if __name__ == '__main__':
    main()