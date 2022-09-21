import tkinter as tk
from tkinter import ttk
from votacion import *
from main import bloqueo, generador_contra
# Definicion de class candidato
# Guarda Atributos de los candidatos
# Para poder generar un boton en votación con sus datos
class Candidato:
    def __init__(self, nom, cargo, lista):
        self.nom = nom      #nombre del candidato
        self.cargo = cargo  #cargo al que se candidata
        self.lista = lista  #lista del candidato

    def __str__(self):
        return f"nombre del candidato: {self.nom}\ncargo del candidato: {self.cargo}\nlista del candidato: {self.lista}"

    def crear_frame_candidato(self, contenedor, id_candidato):
        frame = ttk.Frame(contenedor)

        #configuracion de la grid
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)

        ttk.Label(frame, text=f"Nombre del candidato: {self.nom}").grid(column=0, row=0, padx=5, pady=5)

        ttk.Label(frame, text=f"Cargo al que se postula: {self.cargo}").grid(column=0, row=1, padx=5, pady=5)

        ttk.Label(frame, text=f"Lista: {self.lista}").grid(column=0, row=2, padx=5, pady=5)

        def votar_por():
            with open("resultados_parciales.txt", mode="r") as f:
                f.seek(0)
                contenido = f.readlines()               #leer el archivo
                contenido[0] = str(f"{id_candidato}\n") #modificar la primera linea con el id del candidato elegido
                print(contenido)
                f.writelines(contenido)                 #guardar los cambios

        ttk.Button(frame, text=f"Votar por: {self.nom}", command=votar_por).grid(column=0, row=3, padx=5, pady=5)

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
    ttk.Label(Config, text="Ingresar cantidad de votantes:").grid(column=0, row=0, padx=5, pady=5, sticky=tk.E)

    ttk.Label(Config, text="Ingresar nombre y apellido del candidato:").grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)
    ttk.Label(Config, text="Ingresar cargo al que se candidata:").grid(column=0, row=2, padx=5, pady=5, sticky=tk.E)
    ttk.Label(Config, text="Ingresar lista del candidato:").grid(column=0, row=3, padx=5, pady=5, sticky=tk.E)

    Padron = tk.StringVar()
    ttk.Entry(Config, textvariable=Padron).grid(column=1, row=0, padx=5, pady=5, sticky=tk.EW)

    nom_can = tk.StringVar()
    ttk.Entry(Config, textvariable=nom_can).grid(column=1, row=1, padx=5, pady=5, sticky=tk.EW)
    cargo_can = tk.StringVar()
    ttk.Entry(Config, textvariable=cargo_can).grid(column=1, row=2, padx=5, pady=5, sticky=tk.EW)
    lista_can = tk.StringVar()
    ttk.Entry(Config, textvariable=lista_can).grid(column=1, row=3, padx=5, pady=5, sticky=tk.EW)

    #Boton Agregar Candidatos
    candidatos = []
    def agregar_candidato():
        candidatos.append(Candidato(nom_can.get(), cargo_can.get(), lista_can.get()))
        for candidato in candidatos:
            print(candidato)
        print("fin de lista de candidatos\n")
        nom_can.set("")
        cargo_can.set("")
        lista_can.set("")
    ttk.Button(Config, text="agregar candidato", command=agregar_candidato).grid(column=1, row=5, padx=5, pady=5)


    #Boton Cantidad Votantes
    global contras
    def cantidad_votantes():
        global contras
        global cant_vot
        cant_vot = int(Padron.get())
        print(cant_vot)
        contras = [""] * cant_vot
        print(contras)
        for i in range(cant_vot):
            contras[i] = generador_contra()
        print(contras)

    ttk.Button(Config, text="establecer cantidad de votantes", command=cantidad_votantes,).grid(column=0, columnspan=2, row=4, padx=5, pady=5)


    #Boton Iniciar Votacion
    def bot_vot():
        global contras
        print(contras)
        Config.destroy()
        bloqueo(contras, candidatos)
        # votacion(candidatos)
    ttk.Button(Config, text="iniciar votación", command=bot_vot).grid(column=0, row=5, padx=5, pady=5)

    Config.mainloop()

