import tkinter as tk
from tkinter import ttk
from votacion import *
from config import *

def bloqueo(cantidad_votantes, candidatos):
    contra_votantes = []
    contra_config = "12354678"
    contra_resultados = "87654321"

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
    ttk.Entry(Bloqueo, textvariable=contra).grid(column=1, row=0, padx=5, pady=5, sticky=tk.EW)

    def chequear_contra():
        if contra.get() == contra_config:
            print("sexoooooooooo")
            # config()
            # pass
        elif contra.get() == contra_resultados:
            pass
        else:
            for i in range(len(contra_votantes)):
                if contra == contra_votantes[i]:
                    pass
                else:
                    print("contraseña equivocada")
    ttk.Button(Bloqueo, text="aceptar", command=chequear_contra).grid(column=1, row=1, padx=5, pady=5, sticky=tk.E)

    Bloqueo.mainloop()
