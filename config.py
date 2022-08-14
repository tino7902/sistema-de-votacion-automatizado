import tkinter as tk
from tkinter import ttk
from votacion import *

# Definicion de class candidato
# Guarda Atributos de los candidatos
# Para poder generar un boton en votación con sus datos
class Candidato:
    def __init__(self, nom, cargo, lista):
        self.nom = nom      #nombre del candidato
        self.cargo = cargo  #cargo al que se candidata
        self.lista = lista  #lista del candidato

    def __str__(self):
        #return f"{self.name} is {self.age} years old"
        return f"nombre del candidato: {self.nom}\ncargo del candidato: {self.cargo}\nlista del candidato: {self.lista}"

    def crear_frame_candidato(self, contenedor):
        frame = ttk.Frame(contenedor)

        #configuracion de la grid
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)

        ttk.Label(frame, text=f"Nombre del candidato: {self.nom}").grid(column=0, row=0, padx=5, pady=5)

        ttk.Label(frame, text=f"Nombre del candidato: {self.nom}").grid(column=0, row=1, padx=5, pady=5)

        ttk.Label(frame, text=f"Nombre del candidato: {self.lista}").grid(column=0, row=2, padx=5, pady=5)

        return frame


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
    Config.columnconfigure(1, weight=3)

    #AÑADIR CANDIDATOS
    ttk.Label(Config, text="Ingresar nombre y apellido del candidato:").grid(column=0, row=0, padx=5, pady=5, sticky=tk.E)
    ttk.Label(Config, text="Ingresar cargo al que se candidata:").grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)
    ttk.Label(Config, text="Ingresar lista del candidato:").grid(column=0, row=2, padx=5, pady=5, sticky=tk.E)

    nom_can = tk.StringVar()
    ttk.Entry(Config, textvariable=nom_can).grid(column=1, row=0, padx=5, pady=5, sticky=tk.EW)
    cargo_can = tk.StringVar()
    ttk.Entry(Config, textvariable=cargo_can).grid(column=1, row=1, padx=5, pady=5, sticky=tk.EW)
    lista_can = tk.StringVar()
    ttk.Entry(Config, textvariable=lista_can).grid(column=1, row=2, padx=5, pady=5, sticky=tk.EW)

    candidatos = []
    def agregar_candidato():
        candidatos.append(Candidato(nom_can.get(), cargo_can.get(), lista_can.get()))
        for candidato in candidatos:
            print(candidato)
        print("fin de lista de candidatos\n")
        nom_can.set("")
        cargo_can.set("")
        lista_can.set("")


    ttk.Button(Config, text="agregar candidato", command=agregar_candidato).grid(column=1, row=3, padx=5, pady=5)


    #INICIAR VOTACION
    def bot_vot():
        Config.destroy()
        votacion(candidatos)

    ttk.Button(Config, text="iniciar votación", command=bot_vot).grid(column=0, row=3, padx=5, pady=5)

    Config.mainloop()

