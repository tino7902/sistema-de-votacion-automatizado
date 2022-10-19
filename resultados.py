from main import *
import tkinter as tk
from tkinter import ttk


def crear_frame(contenedor, candidatos, total_votos, votos, i):
    candidato = candidatos[i]
    frame = ttk.Frame(contenedor)
    ttk.Label(contenedor, text=f"Cantidad de votos a favor de {candidato.nom}: {votos[i]}").grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
    porcentaje=(votos[i]*100)/total_votos
    ttk.Label(contenedor, text=f"Porcentaje de votos a favor de {candidato.nom}: {porcentaje}%").grid(row=i, column=1, padx=5, pady=5, sticky=tk.E)
    return frame


def resultados(candidatos, cant_padron):
    print("inicio de ejecucion de resultados")

    with open("resultados_parciales.txt", mode="r") as f:
        contenido = f.readlines()
    # se lee los votos de antes
    votos = contenido[1]
    # se eliminan los carácteres extra
    votos = votos.replace("]", "")
    votos = votos.replace("[", "")
    votos = votos.replace(",", "")
    votos = votos.replace("\n", "")
    # se convierte a una lista
    votos = votos.split(" ")
    # se convierten los elementos de la lista al tipo int
    votos = list(map(int, votos))

    total_votos = 0
    for voto in votos:
        total_votos += voto
    no_votaron = cant_padron - total_votos

    Resultados = tk.Tk()
    window_width = 600
    window_height = 600

    # Centrar Ventana
    # conseguir dimensiones de la pantalla
    screen_width = Resultados.winfo_screenwidth()
    screen_height = Resultados.winfo_screenheight()
    # hallar el centro
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # poner posicion de ventana en el centro de la pantalla
    Resultados.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    Resultados.title("Sistema de Votación Automatizado - Resultados Parciales")

    for i in range(len(candidatos)):
        crear_frame(Resultados, candidatos, total_votos, votos, i).grid(column=1, row=i, columnspan=2, padx=5, pady=5)

    ttk.Label(Resultados, text=f"Cantidad de votos en blanco: {votos[0]}").grid(row=(len(candidatos)+1), column=0, padx=5, pady=5, sticky=tk.W)
    porcentaje=(votos[0]*100)/total_votos
    ttk.Label(Resultados, text=f"Porcentaje de votos en blanco: {porcentaje}%").grid(row=(len(candidatos)+1), column=1, padx=5, pady=5, sticky=tk.E)
    ttk.Label(Resultados, text=f"Cantidad de inscritos en el padron que no votaron: {no_votaron}").grid(row=(len(candidatos)+2), column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
    ttk.Label(Resultados, text=f"Cantidad de inscritos en el padron que sí votaron: {total_votos}").grid(row=(len(candidatos)+3), column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
    porcentaje = (total_votos*100)/cant_padron
    ttk.Label(Resultados, text=f"Porcentaje de inscritos en el padron que sí votaron: {no_votaron}%").grid(row=(len(candidatos)+4), column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
    porcentaje = (no_votaron*100)/cant_padron
    ttk.Label(Resultados, text=f"Porcentaje de inscritos en el padron que no votaron: {no_votaron}%").grid(row=(len(candidatos)+5), column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
    Resultados.mainloop()