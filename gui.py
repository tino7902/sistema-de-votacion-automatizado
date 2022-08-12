import tkinter as tk
from tkinter import ttk

def config():
    print("inicio ejecucion config()")

    config = tk.Tk()
    window_width = 600
    window_height = 600

    #Centrar Ventana
    ## conseguir dimensiones de la pantalla
    screen_width = config.winfo_screenwidth()
    screen_height = config.winfo_screenheight()
    # hallar el centro
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    # poner posicion de ventana en el centro de la pantalla
    config.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    config.title("Sistema de Votación Automatizado - Configuración")

    #Configuracion de la grid
    config.columnconfigure(0, weight=1)
    config.columnconfigure(1, weight=3)

    config.mainloop()

