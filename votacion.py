import tkinter as tk
from tkinter import ttk
from operator import add
import math
from PIL import Image, ImageTk


def votacion(candidatos):
    Votacion = tk.Toplevel()

    Votacion.title("Sistema de Votación Automatizado - Votación")
    Votacion.attributes('-fullscreen', True)

    cant_obj = len(candidatos) + 1
    screen_width = Votacion.winfo_screenwidth()
    canvas_width = math.floor(screen_width / cant_obj)
    canvas_height = math.floor((15 * canvas_width) / 12)
    imagenes = []
    for i in range(len(candidatos)):
        img = Image.open(candidatos[i].foto)
        image = img.resize((math.floor(canvas_width * 0.8), math.floor(canvas_height * 0.5)))
        img_candidato = ImageTk.PhotoImage(image)
        imagenes.append(img_candidato)

    for i in range(len(candidatos)):
        # COLOR DE FONDO
        canvas = tk.Canvas(
            Votacion,
            width=canvas_width,
            height=canvas_height,
            bg="#3897F1"
        )
        canvas.grid(row=0, column=i, ipadx=5, ipady=5)

        # FOTO CANDIDATO
        lbl_img_can = ttk.Label(canvas, borderwidth=0, image=imagenes[i], text="")
        lbl_img_can.place(
            x=canvas_width / 2,
            y=canvas_height * 0.55,
            anchor="s",
            width=canvas_width * 0.8,
            height=canvas_height * 0.5
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
            anchor=tk.N
        )

        # CARGO
        canvas.create_text(
            (canvas_width / 2, canvas_height * 0.7),
            text=candidatos[i].cargo,
            font=("Helvetica", 18),
            anchor=tk.N
        )

        # LISTA
        canvas.create_text(
            (canvas_width / 2, canvas_height * 0.8),
            text=candidatos[i].lista,
            font=("Helvetica", 18),
            anchor=tk.N
        )

        btn_votar = candidatos[i].crear_boton_voto(canvas, i + 1)
        btn_votar.place(x=canvas_width / 2, y=canvas_height * 0.9, anchor="n")

    def voto_blanco():
        with open("resultados_parciales.txt", mode="r") as f:
            contenido = f.readlines()  # leer el archivo
        with open("resultados_parciales.txt", mode="w") as f:
            # modificar la primera linea con el id del candidato elegido
            contenido[0] = "0\n"
            print(contenido)
            f.writelines(contenido)  # guardar los cambios
    img_vb = Image.open("./IMG/img_voto_blanco.jpeg")
    image_vb = img_vb.resize((canvas_width, canvas_height))
    img_voto_blanco = ImageTk.PhotoImage(image_vb)
    btn_voto_blanco = ttk.Button(
        Votacion,
        text="",
        command=voto_blanco,
        image=img_voto_blanco,
    )
    btn_voto_blanco.grid(
        column=len(candidatos) + 1,
        row=0,
        padx=5,
        pady=5
    )

    def confirmar_voto():
        # guardar el contenido del txt en una list contenido
        with open("resultados_parciales.txt", mode="r") as f:
            contenido = f.readlines()

        # list voto_nuevo, cada elemento es 0 menos el del voto elegido
        voto_nuevo = [0] * (len(candidatos) + 1)
        elegido = contenido[0]
        voto_nuevo[int(elegido)] = + 1

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

    img_cv = Image.open("./IMG/img_btn_enviar_voto.jpeg")
    img_conf_voto = ImageTk.PhotoImage(img_cv)
    btn_conf_voto = ttk.Button(
        Votacion,
        text="",
        command=confirmar_voto,
        image=img_conf_voto
    )
    btn_conf_voto.grid(column=0, row=1, padx=5, pady=5, columnspan=2)

    Votacion.mainloop()
