from ssl import VERIFY_ALLOW_PROXY_CERTS
import tkinter as tk
from tkinter import ttk
from config import *

def votacion(candidatos):
    global votos

    votos = [0] * (len(candidatos)+1)

    Votacion = tk.Tk()

    Votacion.title("Sistema de Votación Automatizado - Votación")

    for i in range(len(candidatos)):
        candidatos[i].crear_frame_candidato(Votacion, i+1).grid(column=i, row=0, padx=5, pady=5)
    
    def voto_blanco():
        with open("resultados_parciales.txt", mode="r") as f:
            f.seek(0)
            contenido = f.readlines()               #leer el archivo
        with open("resultados_parciales.txt", mode="w") as f:
            contenido[0] = "0\n"                    #modificar la primera linea con el id del candidato elegido
            print(contenido)
            f.writelines(contenido)                 #guardar los cambios
    ttk.Button(Votacion, text="VOTAR \nEN \nBLANCO", command=voto_blanco).grid(column=len(candidatos)+1, row=0, padx=5, pady=5)

    def confirmar_voto():
        with open("resultados_parciales.txt", mode="r") as f:
            global votos
            f.seek(0)
            contenido = f.readlines()
            elegido = int(contenido[0])
            print(votos)
            votos[elegido] = votos[elegido]+1
            print(votos)
            contenido[1] = str(votos)
        with open("resultados_parciales.txt", mode="w") as f:
            f.writelines(contenido)
        with open("resultados_parciales.txt", mode="r") as f:
            contenido_nuevo = f.readlines()
            print(contenido_nuevo)
        
        Votacion.destroy()

    ttk.Button(Votacion, text="CONFIRMAR VOTO", command=confirmar_voto).grid(column=0, row=1, padx=5, pady=5)

    Votacion.mainloop()