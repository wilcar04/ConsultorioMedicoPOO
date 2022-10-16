import tkinter as tk
from backend.ModeloDelMundo import *
#import uuid


class InterfazGrafica:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1280x720")
        self.window.resizable(False, False)
        self.window.title("Consultorio")
        self.window.config(background="black")

        # Cargar imagen
        self.imagen_boton_registrar = tk.PhotoImage(file="imagenes/1.png")
        self.imagen_boton_eliminar= tk.PhotoImage(file="imagenes/2.png")
        self.imagen_titulo=tk.PhotoImage(file="imagenes/logoo.png",)
        self.imagen_titulo=self.imagen_titulo.subsample(2)

        #Frame Titulo
        self.frame_titulo = tk.Frame(self.window)
        self.frame_titulo.config(background="black")
        self.frame_titulo.grid(row=0, column=0)

        self.label_vacio =tk.Label(self.frame_titulo,text="                                           ",background="black",font=("Candara",30))
        self.label_vacio_2 = tk.Label(self.frame_titulo, text="                                             ",background="black",font=("Candara",30))
        self.label_vacio.grid(row=0, column=0)
        self.label_vacio_2.grid(row=0, column=2)




        #Frame Botones
        self.frame_botones = tk.Frame(self.window)
        self.frame_botones.config(background="black")
        self.frame_botones.grid(row=1, column=0)



        self.label_1 = tk.Label(self.frame_titulo, text="Consultorio")
        self.label_1.config(font=("Candara",48),fg="white",background="black",image=self.imagen_titulo)
        self.label_1.grid(row=0,column=1)

        #Texto respuesta para cuando se registra
        self.label_2 = tk.Label(self.frame_botones)
        self.label_2.config(font="Candara",fg="white",background="black")

        self.boton_1=tk.Button(self.frame_botones,text="Registrar Usuario",command=self.registrar,borderwidth=0,image=self.imagen_boton_registrar)
        self.boton_1.config(font="Candara",fg="white",background="black")
        self.boton_2=tk.Button(self.frame_botones,text="Elimino Usuario",command=self.eliminar_usuario,borderwidth=0,image=self.imagen_boton_eliminar)
        self.boton_2.config(font="Candara", fg="white",background="black")
        #self.boton_3=tk.Button(self.frame_botones,text="Abrir Nueva ventana",command=self.crear_ventana)
        #self.boton_3.config(font="Candara",fg="white",background="black")

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




