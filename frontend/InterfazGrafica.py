import tkinter as tk
from backend.ModeloDelMundo import *
#import uuid


class InterfazGrafica:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1000x900")
        self.window.resizable(False, False)
        self.window.title("Consultorio")
        self.window.config(background="gray16")



        self.frame_prueba_1 = tk.Frame(self.window)
        self.frame_prueba_1.config(background="gray16")
        self.frame_prueba_1.pack()
        self.label_1 = tk.Label(self.frame_prueba_1, text="Consultorio")
        self.label_1.config(font=("Candara",48),fg="white",background="gray16")
        self.label_1.pack()
        #Texto respuesta para cuando se registra
        self.label_2 = tk.Label(self.frame_prueba_1)
        self.label_2.config(font="Candara",fg="white",background="gray16")

        self.boton_1=tk.Button(self.frame_prueba_1,text="Registrar Usuario",command=self.registrar)
        self.boton_1.config(font="Candara",fg="white",background="gray16")
        self.boton_2=tk.Button(self.frame_prueba_1,text="Elimino Usuario",command=self.eliminar_usuario)
        self.boton_2.config(font="Candara", fg="white",background="gray16")
        self.boton_3=tk.Button(self.frame_prueba_1,text="Abrir Nueva ventana",command=self.crear_ventana)
        self.boton_3.config(font="Candara",fg="white",background="gray16")

        #Empaquetar los Botones
        self.boton_1.pack()
        self.boton_2.pack()
        self.boton_3.pack()
        #Ciclo Infinito ventana Principal
        self.window.mainloop()





    def registrar(self):
        mensaje=Mensaje("El usuario ha sido registrado exitosamente")

        self.label_2["text"]=mensaje.mensaje
        self.label_2.pack()

    def eliminar_usuario(self):
        self.label_2["text"]="El usuario ha sido eliminado exitosamente"
        self.label_2.pack()

    def crear_ventana(self):
         self.window_2 = tk.Tk()
         self.window_2.geometry("1000x900")
         self.window_2.resizable(False, False)
         self.window_2.title("Pruebita Ventana :D")

         self.window_2.mainloop()




