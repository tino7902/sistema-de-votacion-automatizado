from ssl import VERIFY_ALLOW_PROXY_CERTS
import tkinter as tk
from tkinter import ttk
from config import *

def votacion(candidatos):
    global votos

    votos = [0] * (len(candidatos)+1)

    Votacion = tk.Tk()

    #Pantalla completa
    ## conseguir dimensiones de la pantalla
    screen_width = Votacion.winfo_screenwidth()
    screen_height = Votacion.winfo_screenheight()
    ## hallar el centro
    center_x = int(screen_width/2)
    center_y = int(screen_height/2)
    ## poner posicion de ventana en el centro de la pantalla
    Votacion.geometry(f'{screen_width}x{screen_height}+{center_x}+{center_y}')

    Votacion.title("Sistema de Votación Automatizado - Votación")
    #configurar grid
    Votacion.rowconfigure(0, weight=3)
    Votacion.rowconfigure(1, weight=1)

    for i in range(len(candidatos)):
        candidatos[i].crear_frame_candidato(Votacion, i+1).grid(column=i, row=0, padx=5, pady=5)
    
    def voto_blanco():
        with open("resultados_parciales.txt", mode="r+") as f:
            f.seek(0)
            contenido = f.readlines()   #leer el archivo
            contenido[0] = "0\n"        #modificar la primera linea con el id del candidato elegido
            print(contenido)
            f.writelines(contenido)     #guardar los cambios
    ttk.Button(Votacion, text="VOTAR \nEN \nBLANCO", command=voto_blanco).grid(column=len(candidatos)+1, row=0, padx=5, pady=5)

    def confirmar_voto():
        with open("resultados_parciales.txt", mode="r+") as f:
            f.seek(0)
            contenido = f.readlines()
            elegido = int(contenido[0])
            votos[elegido] = votos[elegido]+1
            contenido[1] = votos
            f.writelines(contenido)
            contenido_nuevo = f.readlines()
            print(contenido_nuevo)

    ttk.Button(Votacion, text="CONFIRMAR VOTO", command=confirmar_voto).grid(column=0, row=1, padx=5, pady=5)

    Votacion.mainloop()

