import tkinter as tk
from tkinter import ttk
# from main import bloqueo
from resultados import resultados
import string
import random
from PIL import Image, ImageTk


# Para poder generar un boton en votación con sus datos
class Candidato:
    """
    Una class que guarda Atributos de los candidatos

    Atributos
    ----------
    nom : str
        nombre del candidato
    cargo : str
        cargo al que se candidata
    lista : str
        lista a la que se candidata

    Methods
    -------
    crear_frame_candidato(contenedor, id_candidato):
        crea un frame de tkinter para el candidato
    """

    def __init__(self, nom, cargo, lista):
        """
        Construye los atributos necesarios para el objeto Candidato.

        Parametros
        ----------
            nom : str
                nombre del candidato
            cargo : str
                cargo al que se candidata
            lista : str
                lista a la que se candidata
        """

        self.nom = nom
        self.cargo = cargo
        self.lista = lista
        self.bg_lista = Image.open("./IMG/img_lista.jpeg")
        self.lista_bg = ImageTk.PhotoImage(image=self.bg_lista)

    def __str__(self):
        return f"nombre del candidato: {self.nom}\ncargo del candidato: {self.cargo}\nlista del candidato: {self.lista} -- IMAGE: {self.bg_lista} PHOTOIMAGE: {self.lista_bg}"

    def crear_frame_candidato(self, contenedor, id_candidato):
        """
        Crea un frame de tkinter para el candidato

        Parametros
        ----------
            contenedor : ojeto tk
                el contenedor o ventana de tkinter en la que va el frame
            id_candidato : int
                id del candidato al que el frame corresponde

        Retorna
        -------
            frame (ttk.Frame): objeto de tipo frame de tkinter con los datos del candidato
        """

        frame = ttk.Frame(contenedor)

        # configuracion de la grid
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)

        ttk.Label(frame, borderwidth=0, image=self.lista_bg, text="").grid(column=0, row=0, columnspan=2, rowspan=3)

        ttk.Label(frame, text=f"Nombre del candidato: {self.nom}").grid(column=0, row=0, padx=5, pady=5)

        ttk.Label(frame, text=f"Cargo al que se postula: {self.cargo}").grid(column=0, row=1, padx=5, pady=5)

        ttk.Label(frame, text=f"Lista: {self.lista}").grid(column=0, row=2, padx=5, pady=5)

        def votar_por():
            with open("resultados_parciales.txt", mode="r") as f:
                contenido = f.readlines()  # leer el archivo
            with open("resultados_parciales.txt", mode="w") as f:
                # modificar la primera linea con el id del candidato elegido
                contenido[0] = str(f"{id_candidato}\n")
                print(contenido)
                f.writelines(contenido)  # guardar los cambios

        ttk.Button(frame, text=f"Votar por: {self.nom}", command=votar_por).grid(column=0, row=3, padx=5, pady=5)

        return frame


def generador_contra():
    '''
    Devuelve una contraseña aleatoria de 8 letras.

        Returns:
            contra_generada (str): contraseña generada. 8 letras aleatorias
    '''
    # se guardan todas las letras del alfabeto
    letras = string.ascii_lowercase
    # se eligen 8 letras al azar y se devuelve como contraseña
    contra_generada = ''.join(random.choice(letras) for i in range(8))
    return contra_generada


def config(candidatos):
    print("inicio ejecucion Config()")

    Config = tk.Tk()
    window_width = 600
    window_height = 600

    # Centrar Ventana
    # conseguir dimensiones de la pantalla
    screen_width = Config.winfo_screenwidth()
    screen_height = Config.winfo_screenheight()
    # hallar el centro
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # poner posicion de ventana en el centro de la pantalla
    Config.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    Config.title("Sistema de Votación Automatizado - Configuración")

    # Configuracion de la grid
    Config.columnconfigure(0, weight=1)
    Config.columnconfigure(1, weight=3)

    # AÑADIR CANDIDATOS
    ttk.Label(Config, text="Ingresar cantidad de votantes:").grid(
        column=0, row=0, padx=5, pady=5, sticky=tk.E)

    ttk.Label(Config, text="Ingresar nombre y apellido del candidato:").grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)
    ttk.Label(Config, text="Ingresar cargo al que se candidata:").grid(column=0, row=2, padx=5, pady=5, sticky=tk.E)
    ttk.Label(Config, text="Ingresar lista del candidato:").grid(column=0, row=3, padx=5, pady=5, sticky=tk.E)

    Padron = tk.StringVar(Config)
    ttk.Entry(Config, textvariable=Padron).grid(column=1, row=0, padx=5, pady=5, sticky=tk.EW)

    nom_can = tk.StringVar(Config)
    ttk.Entry(Config, textvariable=nom_can).grid(column=1, row=1, padx=5, pady=5, sticky=tk.EW)
    cargo_can = tk.StringVar(Config)
    ttk.Entry(Config, textvariable=cargo_can).grid(column=1, row=2, padx=5, pady=5, sticky=tk.EW)
    lista_can = tk.StringVar(Config)
    ttk.Entry(Config, textvariable=lista_can).grid(column=1, row=3, padx=5, pady=5, sticky=tk.EW)

    # Boton Agregar Candidatos
    def agregar_candidato():
        candidatos.append(Candidato(nom_can.get(), cargo_can.get(), lista_can.get()))
        for candidato in candidatos:
            print(candidato)
        print("fin de lista de candidatos\n")
        nom_can.set("")
        cargo_can.set("")
        lista_can.set("")
    ttk.Button(Config, text="agregar candidato", command=agregar_candidato).grid(
        column=1, row=4, padx=5, pady=5)

    # Boton Cantidad Votantes
    global contras

    def cantidad_votantes():
        global contras
        global cant_vot
        cant_vot = int(Padron.get())
        Padron.set("")
        print(cant_vot)
        contras = [""] * cant_vot
        print(contras)
        for i in range(cant_vot):
            contras[i] = generador_contra()
        print(contras)
    ttk.Button(Config, text="establecer cantidad de votantes", command=cantidad_votantes,).grid(
        column=0, row=4, padx=5, pady=5)

    # Boton Iniciar Votacion
    def bot_vot():
        from main import bloqueo
        global contras
        print(contras)
        Config.destroy()
        bloqueo(contras, candidatos)
    ttk.Button(Config, text="iniciar votación", command=bot_vot).grid(column=0, row=5, padx=5, pady=5)

    def bot_resultados():
        Config.destroy()
        resultados(candidatos, cant_vot)
    ttk.Button(Config, text="ver resultados", command=bot_resultados).grid(column=1, row=5, padx=5, pady=5)

    Config.mainloop()
