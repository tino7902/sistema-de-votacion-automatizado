import tkinter as tk
from tkinter import ttk
from operator import add
import math
from PIL import Image, ImageTk


def votacion(candidatos):
    Votacion = tk.Toplevel()

    # Título de ventana + fullscreen
    Votacion.title("Sistema de Votación Automatizado - Votación")
    Votacion.attributes("-fullscreen", True)

    # DECLARACION DE VARIABLES PARA DESPUES
    cant_obj = len(candidatos) + 1  # Cantidad de opciones para votar
    screen_width = Votacion.winfo_screenwidth()  # Ancho de la pantalla
    canvas_width = math.floor(screen_width / cant_obj)  # Ancho para el canvas
    canvas_height = math.floor((15 * canvas_width) / 12)  # Alto del canvas
    imagenes = []  # Lista que contendrá todas las imagenes
    # lista con imagenes iguales para cada boton, no pregunten porque...
    images_votar = []

    # Se guarda la foto de cada candidato en una lista para evitar que se sobreescriban
    # Se tiene porque sino solo aparece la última imagen
    for i in range(len(candidatos)):
        img = Image.open(candidatos[i].foto)
        image = img.resize(
            (math.floor(canvas_width * 0.8), math.floor(canvas_height * 0.5))
        )
        img_candidato = ImageTk.PhotoImage(image)
        imagenes.append(img_candidato)

        img_votar = Image.open("./IMG/img_btn_votar.jpeg")  # tamaño de la img: 345x1280
        image_votar = ImageTk.PhotoImage(img_votar)
        images_votar.append(image_votar)

    # Se crea un canvas para cada candidato
    # Contiene su foto, nombre, cargo, lista y un botón para votarlo
    for i in range(len(candidatos)):
        # COLOR DE FONDO
        canvas = tk.Canvas(
            Votacion, width=canvas_width, height=canvas_height, bg="#3897F1"
        )
        canvas.grid(row=0, column=i, ipadx=5, ipady=5)

        # FOTO CANDIDATO
        lbl_img_can = ttk.Label(canvas, borderwidth=0, image=imagenes[i], text="")
        lbl_img_can.place(
            x=canvas_width / 2,
            y=canvas_height * 0.55,
            anchor="s",
            width=canvas_width * 0.8,
            height=canvas_height * 0.5,
        )

        # NOMBRE CANDIDATO
        if len(candidatos[i].nom) <= 20:
            font_nombre = ("Helvetica", 28)
        else:
            font_nombre = ("Helvetica", 24)
        canvas.create_text(
            (canvas_width / 2, canvas_height * 0.6),
            text=candidatos[i].nom,
            font=font_nombre,
            anchor=tk.N,
        )

        # CARGO
        canvas.create_text(
            (canvas_width / 2, canvas_height * 0.7),
            text=candidatos[i].cargo,
            font=("Helvetica", 18),
            anchor=tk.N,
        )

        # LISTA
        canvas.create_text(
            (canvas_width / 2, canvas_height * 0.75),
            text=candidatos[i].lista,
            font=("Helvetica", 18),
            anchor=tk.N,
        )

        # BOTÓN PARA VOTAR

        btn_votar = candidatos[i].crear_boton_voto(canvas, i + 1, images_votar[i])
        btn_votar.place(
            x=canvas_width / 2,
            y=canvas_height * 0.85,
            anchor="n",
        )

    # Función para el voto en blanco
    def voto_blanco():
        with open("resultados_parciales.txt", mode="r") as f:
            contenido = f.readlines()  # leer el archivo
        with open("resultados_parciales.txt", mode="w") as f:
            # modificar la primera linea con el id del candidato elegido
            # (0 para voto en blanco)
            contenido[0] = "0\n"
            print(contenido)
            f.writelines(contenido)  # guardar los cambios

    # Configuración del botón para voto en blanco
    img_vb = Image.open("./IMG/img_voto_blanco.jpeg")  # tamaño de la img: 345x1280
    # se calcula las nuevas dimensiones de la img
    vb_height = math.floor(canvas_height)  # la nueva altura sera la del canvas
    vb_width = math.floor(
        (345 * canvas_height) / 1280
    )  # regla de tres para hallar el ancho
    image_vb = img_vb.resize((vb_width, vb_height))
    img_voto_blanco = ImageTk.PhotoImage(image_vb)
    btn_voto_blanco = ttk.Button(
        Votacion,
        text="",
        command=voto_blanco,
        image=img_voto_blanco,
    )
    btn_voto_blanco.grid(column=len(candidatos) + 1, row=0, padx=5, pady=5)

    def confirmar_voto():
        # guardar el contenido del txt en una list contenido
        with open("resultados_parciales.txt", mode="r") as f:
            contenido = f.readlines()

        # list voto_nuevo, cada elemento es 0 menos el del voto elegido
        voto_nuevo = [0] * (len(candidatos) + 1)
        elegido = contenido[0]
        voto_nuevo[int(elegido)] = +1

        # si es el primer voto, cada elemento de list votos_antes es 0
        if contenido[1] == "primera vez":
            votos_antes = [0] * (len(candidatos) + 1)

        # sino se lee desde el txt
        else:
            # se lee los votos de antes
            votos_antes = contenido[1]
            # se eliminan los carácteres extra
            votos_antes = votos_antes.replace("]", "")
            votos_antes = votos_antes.replace("[", "")
            votos_antes = votos_antes.replace(",", "")
            votos_antes = votos_antes.replace("\n", "")
            # se convierte a una lista
            votos_antes = votos_antes.split(" ")
            # se convierten los elementos de la lista al tipo int
            votos_antes = list(map(int, votos_antes))

        # se suman los votos viejos más el nuevo
        print(voto_nuevo)
        print(votos_antes)
        votos_ahora = list(map(add, votos_antes, voto_nuevo))
        print(votos_ahora)

        # se actualiza el txt
        contenido[1] = f"{str(votos_ahora)}\n"
        print(contenido)
        with open("resultados_parciales.txt", mode="w") as f:
            f.writelines(contenido)

        Votacion.destroy()

    # Configuración del boton de confirmar voto
    img_cv = Image.open("./IMG/img_btn_enviar_voto.jpeg")
    img_conf_voto = ImageTk.PhotoImage(img_cv)
    btn_conf_voto = ttk.Button(
        Votacion, text="", command=confirmar_voto, image=img_conf_voto
    )
    btn_conf_voto.grid(column=0, row=1, padx=5, pady=5, columnspan=2)

    Votacion.mainloop()
