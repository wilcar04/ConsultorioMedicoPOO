import tkinter as tk
from backend.ModeloDelMundo import *
from frontend import *
#import uuid


class InterfazGrafica:
    def __init__(self,nombre:str):
        self.nombre=nombre
    def crear_ventana_principal(self):
        self.window = tk.Tk()
        self.window.geometry("1280x720")
        self.window.resizable(False, False)
        self.window.title("Consultorio")
        self.window.config(background="black")

        # Cargar imagen
        self.imagen_boton_registrar = tk.PhotoImage(file="imagenes/btn_registrar_usuario.png")
        self.imagen_boton_eliminar= tk.PhotoImage(file="imagenes/btn_eliminar_usuario.png")
        self.imagen_titulo=tk.PhotoImage(file="imagenes/logo_titulo.png" )
        #Disminuir escala imagen
        self.imagen_titulo=self.imagen_titulo.subsample(2)

        #Frame Titulo
        self.frame_titulo = tk.Frame(self.window)
        self.frame_titulo.config(background="black")
        self.frame_titulo.grid(row=0, column=0)

        #Labels vacios para centrar Titulo
        self.label_vacio =tk.Label(self.frame_titulo,text="                                           ",background="black",font=("Candara",30))
        self.label_vacio_2 = tk.Label(self.frame_titulo, text="                                             ",background="black",font=("Candara",30))
        self.label_vacio.grid(row=0, column=0)
        self.label_vacio_2.grid(row=0, column=2)




        #Frame Botones
        self.frame_botones = tk.Frame(self.window)
        self.frame_botones.config(background="black")
        self.frame_botones.grid(row=1, column=0)


        #Titulo -> Logo
        self.label_1 = tk.Label(self.frame_titulo, text="Consultorio")
        self.label_1.config(font=("Candara",48),fg="white",background="black",image=self.imagen_titulo)
        self.label_1.grid(row=0,column=1)

        #Texto respuesta para cuando se registra
        self.label_2 = tk.Label(self.frame_botones)
        
        self.label_2.config(font="Candara",fg="white",background="black")

        self.boton_1=tk.Button(self.frame_botones,text="Registrar Usuario",borderwidth=0,image=self.imagen_boton_registrar,command=self.registrar)
        self.boton_1.config(font="Candara",fg="white",background="black")
        self.boton_2=tk.Button(self.frame_botones,text="Elimino Usuario",command=self.eliminar_usuario,borderwidth=0,image=self.imagen_boton_eliminar)
        self.boton_2.config(font="Candara", fg="white",background="black")


        #Empaquetar los Botones
        self.boton_1.pack()
        self.boton_2.pack()

        self.window.mainloop()






    def registrar(self):
     self.ventana_registrar=tk.Toplevel()
     self.ventana_registrar.geometry("1280x720")
     self.ventana_registrar.title("Registrar")
     self.ventana_registrar.resizable(False, False)
     self.ventana_registrar.config(background="black")

     self.frame_titulo_registrar=tk.Frame(self.ventana_registrar)
     self.frame_botones_registrar = tk.Frame(self.ventana_registrar)
     self.frame_botones_registrar.config(background="black")
     self.frame_titulo_registrar.config(background="black")
     self.frame_titulo_registrar.grid(row=0, column=0)
     self.frame_botones_registrar.grid(row=0,column=0)
     self.label_vacio_registrar = tk.Label(self.frame_titulo_registrar, text="                                           ",
                                 background="black", font=("Candara", 30))
     self.label_vacio_registrar2 = tk.Label(self.frame_titulo_registrar, text="                                             ",
                                   background="black", font=("Candara", 30))
     self.label_vacio_registrar.grid(row=0, column=0)
     self.label_vacio_registrar2.grid(row=0, column=2)

     # Titulo -> Logo
     self.label_registrar = tk.Label(self.frame_titulo_registrar, text="Consultorio")
     self.label_registrar.config(font=("Candara", 48), fg="white", background="black", image=self.imagen_titulo)
     self.label_registrar.grid(row=0, column=1)







    def eliminar_usuario(self):
        self.label_2["text"]="El usuario ha sido eliminado exitosamente"
        self.label_2.pack()




