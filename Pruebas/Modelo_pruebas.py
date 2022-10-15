import tkinter as tk
from tkinter import font


def obtener_fuentes_tk():
    root = tk.Tk()
    root.title("Tipos de Fuentes")
    fuente=list(font.families())
    for f in fuente:
        print(f"Esta es una Fuente {f}")
    return fuente

"""Links:
https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/widget-label-etiqueta-de-texto/
https://es.stackoverflow.com/questions/330481/fuentes-disponibles-en-tkinter
https://github.com/JevDev2304/EjercicioBlackJackApp-master/blob/master/juego/ui/Interfaztk.py"""

