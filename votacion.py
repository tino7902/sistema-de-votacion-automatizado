import tkinter as tk
from tkinter import ttk

def votacion():
    Votacion = tk.Tk()
    window_width = 600
    window_height = 600

    #Centrar Ventana
    ## conseguir dimensiones de la pantalla
    screen_width = Votacion.winfo_screenwidth()
    screen_height = Votacion.winfo_screenheight()
    # hallar el centro
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    # poner posicion de ventana en el centro de la pantalla
    Votacion.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    Votacion.title("Sistema de Votación Automatizado - Votación")
    Votacion.mainloop()