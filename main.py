from config import config
from votacion import *
from resultados import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def main():
    """
    Inicializa el programa.
    Formatea resultados_parciales.txt.
    Inicia ventana de Bloqueo
    """
    candidatos = []  # lista de candidatos
    contras = []  # lista de contraseñas generadas

    # formatear el txt
    with open("resultados_parciales.txt", mode="w") as f:
        f.write("elegido: \nprimera vez")
    # iniciar la ventana de bloqueo
    bloqueo(contras, candidatos)


def bloqueo(contras, candidatos):
    """
    Pantalla inicial y la más usada.
    Bloquea la votacion hasta que se ingrese una de las contraseñas.

        Parametros:
            contras (list): lista de las contraseñas
            condidatos (list): lista de los candidatos
    """

    Bloqueo = tk.Tk()

    # se hace que la ventana sea pantalla completa
    Bloqueo.attributes("-fullscreen", True)

    # configuracion de la grid
    Bloqueo.grid_rowconfigure(0, weight=1)
    Bloqueo.grid_rowconfigure(2, weight=1)
    Bloqueo.grid_columnconfigure(0, weight=1)
    Bloqueo.grid_columnconfigure(2, weight=1)

    # titulo de la ventana
    Bloqueo.title("Sistema de Votación Automatizado")

    # label con la imagen de fondo + entry donde se escribe la contraseña
    ttk.Label(text="", borderwidth=0).grid(column=0, row=0)
    contra = tk.StringVar()
    ing_contra_img = ImageTk.PhotoImage(file="./IMG/img_ingresar_contra.jpeg")
    print(ing_contra_img)
    ttk.Label(Bloqueo, borderwidth=0, image=ing_contra_img, text="").grid(
        column=1, row=0, padx=5, pady=5
    )
    ttk.Entry(Bloqueo, textvariable=contra, show="*").grid(
        column=1, row=0, padx=5, pady=5
    )

    def chequear_contra():
        """Chequea la contraseña ingresada y abre la ventana correspondiente."""

        # se guarda la contraseña en una variable para compararla
        contra_ingresada = contra.get()
        contra.set("")
        # ADMIN
        contra_admin = "admin"  # CAMBIAR ESTA VARIABLE PARA CAMBIAR LA CONTRA DE ADMIN
        if contra_ingresada == contra_admin:
            print("contraseña config")
            Bloqueo.destroy()
            config(candidatos)
        # VOTANTES
        else:
            for i in range(len(contras)):
                if contra_ingresada == contras[i]:
                    print("contraseña correcta")
                    contras.remove(contra_ingresada)
                    print(contras)
                    votacion(candidatos)
                else:
                    print("contraseña equivocada")

    # Boton de confirmación + imagen
    img = Image.open("./IMG/img_btn_confirmar.jpeg")
    img_confirmar = ImageTk.PhotoImage(img)
    ttk.Button(Bloqueo, text="", command=chequear_contra, image=img_confirmar).grid(
        column=1, row=1, padx=5, pady=5, sticky=tk.N
    )

    Bloqueo.mainloop()


if __name__ == "__main__":
    main()
