import tkinter as tk
from tkinter import font
import os


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
def pepe():
    os.startfile(r"C:\Users\jvald\OneDrive\Escritorio\InterfazgraficaPOO\frontend\files\historia_medica.txt")
    pregunta=int(input("¿"))
    if pregunta==1:
        archivo=open(r"C:\Users\jvald\OneDrive\Escritorio\InterfazgraficaPOO\frontend\files\historia_medica.txt")
        texto=archivo.read()
        print(texto)

archivo=open(r"C:\Users\jvald\OneDrive\Escritorio\InterfazgraficaPOO\frontend\files\historia_medica.txt","w",encoding="utf-8")
archivo.write("""HISTORIA CLINICA 
Nombre:
Edad :
Sexo :
Ocupación :
Previsión :
Domicilio :
ANAMNESIS ACTUAL:





ANAMNESIS REMOTA:


Antecedentes mórbidos:



Revisión por sistemas:



Respiratorios : 



Examen Físico:



General:







Examen físico segmentario:
Cabeza:


Cara:


Boca:


Cuello:



Tórax:




Abdomen:



Extremidades:







Vascular:



Neurológico periférico:



Columna:

""")
archivo.close()
