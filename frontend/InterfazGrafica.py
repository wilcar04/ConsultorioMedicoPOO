import tkinter as tk
from backend.ModeloDelMundo import *
#import uuid


class InterfazGrafica:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1000x900")
        self.window.resizable(False, False)
        self.window.title("Pruebita XD")



        self.frame_prueba_1 = tk.Frame(self.window)
        self.frame_prueba_1.pack()
        self.label_1 = tk.Label(self.frame_prueba_1, text="PROBANDO INTERFAZ")
        self.label_1.pack()
        self.label_2= tk.Label(self.frame_prueba_1)
        self.boton_1=tk.Button(self.frame_prueba_1,text="Soy un Boton",command=self.saludar)
        self.boton_1.pack()
        self.boton_2=tk.Button(self.frame_prueba_1,text="Elimino",command=self.eliminar_label_saludar)
        self.boton_2.pack()
        self.boton_3=tk.Button(self.frame_prueba_1,text="Abro Nueva ventana OwO",command=self.cambiar_ventana)
        self.boton_3.pack()
        self.window.mainloop()





    def saludar(self):
        mensaje=Mensaje("Hola soy un mensaje y existo")
        self.label_2.pack()
        self.label_2["text"]=mensaje.mensaje
    def eliminar_label_saludar(self):
        self.label_2.pack()
        self.label_2["text"]=""

    def cambiar_ventana(self):
         self.window_2 = tk.Tk()
         self.window_2.geometry("1000x900")
         self.window_2.resizable(False, False)
         self.window_2.title("Pruebita Ventana :D")

         self.window_2.mainloop()




