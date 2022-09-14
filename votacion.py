from ssl import VERIFY_ALLOW_PROXY_CERTS
import tkinter as tk
from tkinter import ttk
from config import *

def votacion(candidatos):
    global votos
    global elegido
    votos = [""] * (len(candidatos)+1)

    Votacion = tk.Tk()
    window_width = 600
    window_height = 600

    #Centrar Ventana
    ## conseguir dimensiones de la pantalla
    screen_width = Votacion.winfo_screenwidth()
    screen_height = Votacion.winfo_screenheight()
    ## hallar el centro
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    ## poner posicion de ventana en el centro de la pantalla
    Votacion.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    Votacion.title("Sistema de Votación Automatizado - Votación")
    #configurar grid
    Votacion.rowconfigure(0, weight=3)
    Votacion.rowconfigure(1, weight=1)

    for i in range(len(candidatos)):
        candidatos[i].crear_frame_candidato(Votacion).grid(column=i, row=0, padx=5, pady=5)
    
    def voto_blanco():
        global votos
        global elegido
        elegido = 0
    ttk.Button(Votacion, text="VOTAR \nEN \nBLANCO", command=voto_blanco).grid(column=len(candidatos)+1, row=0, padx=5, pady=5)

    def confirmar_voto():
        # global votos
        # global cant_vot
        global elegido
        print(elegido)
    ttk.Button(Votacion, text="CONFIRMAR VOTO", command=confirmar_voto).grid(column=0, row=1, padx=5, pady=5)

    Votacion.mainloop()

