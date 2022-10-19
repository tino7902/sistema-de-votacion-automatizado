import tkinter as tk
from tkinter import ttk
from operator import add


def votacion(candidatos):
    Votacion = tk.Tk()

    Votacion.title("Sistema de Votación Automatizado - Votación")
    window_width = 1200
    window_height = 600

    # Centrar Ventana
    # conseguir dimensiones de la pantalla
    screen_width = Votacion.winfo_screenwidth()
    screen_height = Votacion.winfo_screenheight()
    # hallar el centro
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # poner posicion de ventana en el centro de la pantalla
    Votacion.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    for i in range(len(candidatos)):
        candidatos[i].crear_frame_candidato(Votacion, i + 1).grid(column=i, row=0, padx=5, pady=5)

    def voto_blanco():
        with open("resultados_parciales.txt", mode="r") as f:
            contenido = f.readlines()  # leer el archivo
        with open("resultados_parciales.txt", mode="w") as f:
            # modificar la primera linea con el id del candidato elegido
            contenido[0] = "0\n"
            print(contenido)
            f.writelines(contenido)  # guardar los cambios
    ttk.Button(Votacion, text="VOTAR \nEN \nBLANCO", command=voto_blanco).grid(column=len(candidatos) + 1, row=0, padx=5, pady=5)

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

    ttk.Button(Votacion, text="CONFIRMAR VOTO", command=confirmar_voto).grid(
        column=0, row=1, padx=5, pady=5)

    Votacion.mainloop()
