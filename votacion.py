from os import truncate
from ssl import VERIFY_ALLOW_PROXY_CERTS
import tkinter as tk
from tkinter import ttk
from config import *

def votacion(candidatos):
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
            contenido = f.readlines()
        if contenido[2] == "primera vez\n":
            global votos
            votos = [0] * (len(candidatos)+1)
            elegido = contenido[0]
            votos[int(elegido)] =+ 1
            contenido[1] = str(votos)
            contenido[2] = ""
        else:
            votos = contenido[1]
            votos = votos.replace("[", "")
            votos = votos.replace("]", "")
            votos = votos.replace(",", "")
            votos = votos.replace("\n", "")
            votos = votos.split(" ")

        Votacion.destroy()

    ttk.Button(Votacion, text="CONFIRMAR VOTO", command=confirmar_voto).grid(column=0, row=1, padx=5, pady=5)

    Votacion.mainloop()