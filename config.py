import tkinter as tk
from tkinter import ttk
from votacion import *

def config():
    print("inicio ejecucion Config()")

    Config = tk.Tk()
    window_width = 600
    window_height = 600

    #Centrar Ventana
    ## conseguir dimensiones de la pantalla
    screen_width = Config.winfo_screenwidth()
    screen_height = Config.winfo_screenheight()
    # hallar el centro
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    # poner posicion de ventana en el centro de la pantalla
    Config.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    Config.title("Sistema de Votación Automatizado - Configuración")

    #Configuracion de la grid
    Config.columnconfigure(0, weight=1)
    Config.columnconfigure(1, weight=1)
    Config.columnconfigure(2, weight=1)

    def bot_vot():
        Config.destroy()
        votacion()

    ttk.Button(Config, text="iniciar votación", command=bot_vot).grid(column=1, row=1, padx=5, pady=5)

    Config.mainloop()

