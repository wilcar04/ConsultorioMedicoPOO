import tkinter as tk
from backend.ModeloDelMundo import *
from tkinter import messagebox
from datetime import *
from frontend import *

informacion=Informacion()

class InterfazGrafica:
    def __init__(self,nombre:str):
        self.nombre=nombre
    def crear_ventana_principal(self):
        self.window = tk.Tk()
        self.window.iconbitmap("imagenes/logo_ventana.ico")
        self.window.geometry("1280x820")
        self.window.resizable(False, False)
        self.window.title("Consultorio")
        self.window.config(background="black")
        self.window.maxsize(1280,720)

        # Cargar imagen

        self.imagen_titulo=tk.PhotoImage(file="imagenes/logo_titulo.png" )
        self.imagen_boton_registrar_nombre=tk.PhotoImage(file="imagenes/btn_nombre_registrar.png")
        self.imagen_boton_registrar_registrar=tk.PhotoImage(file="imagenes/btn_registrar_registrar.png")
        self.imagen_boton_eliminar_eliminar=tk.PhotoImage(file="imagenes/lbl_eliminar_eliminar_usuario.png")
        self.imagen_boton_registrar_cita=tk.PhotoImage(file="imagenes/btn_registrar_cita.png")

        self.imagen_boton_registrar_cedula=tk.PhotoImage(file="imagenes/btn_cedula_registrar.png")
        self.imagen_boton_registrar_sexo=tk.PhotoImage(file="imagenes/btn_sexo_registrar.png")
        self.imagen_boton_registrar_fecha=tk.PhotoImage(file="imagenes/btn_fecha_registrar.png")
        self.imagen_boton_registrar_celular=tk.PhotoImage(file="imagenes/btn_registrar_celular.png")
        self.imagen_boton_volver_menu_registrar=tk.PhotoImage(file="imagenes/btn_registrar_volver_menu.png")

        self.imagen_label_fecha_registrar_cita=tk.PhotoImage(file="imagenes/lbl_fecha_registrar_cita.png")
        self.imagen_label_hora_registrar_cita=tk.PhotoImage(file="imagenes/lbl_hora_registrar_cita.png")


        #Disminuir escala imagen
        self.imagen_titulo=self.imagen_titulo.subsample(2)
        self.imagen_titulo_pequena=self.imagen_titulo.subsample(2)


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

        self.boton_1=tk.Button(self.frame_botones,text="Registrar Usuario",borderwidth=0,image=self.imagen_boton_registrar_registrar,command=self.registrar)
        self.boton_1.config(font="Candara",fg="white",background="black")
        self.boton_2=tk.Button(self.frame_botones,text="Elimino Usuario",command=self.eliminar,borderwidth=0,image=self.imagen_boton_eliminar_eliminar)
        self.boton_2.config(font="Candara", fg="white",background="black")
        self.boton_3=tk.Button(self.frame_botones, text="Registrar Cita",borderwidth=0,image=self.imagen_boton_registrar_cita,command=self.registrar_cita)
        self.boton_3.config(font="Candara",fg="white",background="black")


        #Empaquetar los Botones
        self.boton_1.grid(row=0,column=1)
        self.boton_2.grid(row=0, column=2)
        self.boton_3.grid(row= 1,column=1)

        self.window.mainloop()






    def registrar(self):
     self.window.withdraw()
     self.ventana_registrar=tk.Toplevel()
     self.ventana_registrar.iconbitmap("imagenes/logo_ventana.ico")
     self.ventana_registrar.geometry("1280x820")
     self.ventana_registrar.title("Registrar")
     self.ventana_registrar.resizable(False, False)
     self.ventana_registrar.config(background="black")

     self.frame_titulo_registrar=tk.Frame(self.ventana_registrar)
     self.frame_botones_registrar = tk.Frame(self.ventana_registrar)
     self.frame_boton_padre_registrar=tk.Frame(self.ventana_registrar)
     self.frame_botones_registrar.config(background="black")
     self.frame_titulo_registrar.config(background="black")
     self.frame_boton_padre_registrar.config(background="black")
     self.frame_titulo_registrar.grid(row=0, column=0)
     self.frame_botones_registrar.grid(row=1,column=0)
     self.frame_boton_padre_registrar.grid(row=2,column=0)


     self.label_vacio_registrar = tk.Label(self.frame_titulo_registrar, text="                                                         ",
                                 background="black", font=("Candara", 30))
     self.label_vacio_registrar2 = tk.Label(self.frame_titulo_registrar, text="                                                         ",
                                   background="black", font=("Candara", 30))
     self.label_vacio_registrar.grid(row=0, column=0)
     self.label_vacio_registrar2.grid(row=0, column=2)

     # Titulo -> Logo
     self.label_registrar = tk.Label(self.frame_titulo_registrar, text="Consultorio")
     self.label_registrar.config(font=("Candara", 48), fg="white", background="black", image=self.imagen_titulo_pequena)
     self.label_registrar.grid(row=0, column=1)
     #Entradas -> info
     self.nombre_registrar=tk.Label(self.frame_botones_registrar)
     self.nombre_registrar.config(font=("Candara",48),fg="white",background="black",image=self.imagen_boton_registrar_nombre)
     self.nombre_registrar.grid(row=2,column=0)
     self.entrada_nombre=tk.Entry(self.frame_botones_registrar,font="Candara",bd=4,width=30, justify="center")
     self.entrada_nombre.grid(row=2,column=1)

     self.cedula_registrar=tk.Label(self.frame_botones_registrar)
     self.cedula_registrar.config(font=("Candara",48),fg="white",background="black",image=self.imagen_boton_registrar_cedula)
     self.cedula_registrar.grid(row=3,column=0)
     self.entrada_cedula=tk.Entry(self.frame_botones_registrar,font="Candara",bd=4,width=30, justify="center")
     self.entrada_cedula.grid(row=3,column=1)

     self.genero_registrar = tk.Label(self.frame_botones_registrar)
     self.genero_registrar.config(font=("Candara", 48), fg="white", background="black",image=self.imagen_boton_registrar_sexo)
     self.genero_registrar.grid(row=4, column=0)
     self.entrada_genero= tk.Entry(self.frame_botones_registrar, font="Candara", bd=4, width=30, justify="center")
     self.entrada_genero.grid(row=4, column=1)

     self.fecha_registrar = tk.Label(self.frame_botones_registrar)
     self.fecha_registrar.config(font=("Candara", 48), fg="white", background="black",image=self.imagen_boton_registrar_fecha)
     self.fecha_registrar.grid(row=5, column=0)
     self.entrada_fecha= tk.Entry(self.frame_botones_registrar, font="Candara", bd=4, width=30, justify="center")
     self.entrada_fecha.grid(row=5, column=1)

     self.celular_registrar = tk.Label(self.frame_botones_registrar)
     self.celular_registrar.config(font=("Candara", 48), fg="white", background="black",image=self.imagen_boton_registrar_celular)
     self.celular_registrar.grid(row=6, column=0)
     self.entrada_celular = tk.Entry(self.frame_botones_registrar, font="Candara", bd=4, width=30, justify="center")
     self.entrada_celular.grid(row=6, column=1)

     self.boton_obtener_info= tk.Button(self.frame_boton_padre_registrar,borderwidth=0,image=self.imagen_boton_registrar_registrar,background="black",command=self.obtener_info)
     self.boton_obtener_info.grid(row=0,column=1)


     self.boton_devolverse= tk.Button(self.frame_boton_padre_registrar,borderwidth=0,image=self.imagen_boton_volver_menu_registrar,background="black",command=self.devolverse_registrar_a_menu)
     self.boton_devolverse.grid(row=0,column=0)

     self.ventana_registrar.mainloop()


    def obtener_info(self):
        try:
            nombre=self.entrada_nombre.get()
            cedula=self.entrada_cedula.get()
            sexo=self.entrada_genero.get()
            fecha=self.entrada_fecha.get()
            celular=self.entrada_celular.get()
            nombre=nombre.replace(" ","")
            verificacion_nombre=nombre.isalpha()
            verificacion_cedula=cedula.isdigit()
            verificar_fecha=datetime.strptime(fecha,"%d/%m/%Y")
            verificacion_sexo=sexo.isalpha()
            verificar_celular=celular.isdigit()
            if verificacion_nombre==False:
                raise Exception("No ingresaste bien el nombre.")
            if verificacion_cedula is False and len(cedula)<=10:
                raise Exception("No ingresaste bien la cedula.")
            if verificacion_sexo is False:
                raise Exception("No ingresaste bien el sexo.")
            if verificar_celular is False:
                raise Exception("No ingresaste Bien la fecha.")
        except ValueError as error:
            tk.messagebox.showwarning("Mala digitación",str(error))
        except Exception as error:
            tk.messagebox.showwarning("Mala digitaciòn",f"{str(error)}")
        else:
            diccionario={"nombre":nombre, "cedula":cedula,"sexo":sexo,"fecha":fecha,"celular":celular}
            paciente=Paciente(nombre,cedula,sexo,fecha,celular)
            tk.messagebox.showinfo("Registro"," El registro se hizo sin problemas")
            self.ventana_registrar.destroy()
            self.window.iconify()
            self.window.state("zoomed")
            informacion.agregrar_informacion_registrar(diccionario)
            return paciente
    def devolverse_registrar_a_menu(self):
        self.ventana_registrar.destroy()
        self.window.iconify()
        self.window.state("zoomed")
    def devolverse_eliminar_a_menu(self):
        self.ventana_eliminar.destroy()
        self.window.iconify()
        self.window.state("zoomed")
    def devolverse_registrar_cita_a_menu(self):
        self.ventana_registrar_cita.destroy()
        self.window.iconify()
        self.window.state("zoomed")





    def eliminar(self):
        self.window.withdraw()

        self.ventana_eliminar = tk.Toplevel()
        self.ventana_eliminar.iconbitmap("imagenes/logo_ventana.ico")
        self.ventana_eliminar.geometry("1280x420")
        self.ventana_eliminar.title("Eliminar")
        self.ventana_eliminar.resizable(False, False)
        self.ventana_eliminar.config(background="black")

        self.frame_titulo_eliminar = tk.Frame(self.ventana_eliminar)
        self.frame_titulo_eliminar.config(background="black")
        self.frame_botones_eliminar = tk.Frame(self.ventana_eliminar)
        self.frame_botones_eliminar.config(background="black")
        self.frame_titulo_eliminar.grid(row=0, column=1)
        self.frame_botones_eliminar.grid(row=1,column=1)


        self.label_eliminar= tk.Label(self.frame_titulo_eliminar, text="Consultorio")
        self.label_eliminar.config(font=("Candara", 48), fg="white", background="black",
                                    image=self.imagen_titulo_pequena)
        self.label_eliminar.grid(row=0, column=1)

        self.label_vacio_eliminar = tk.Label(self.frame_titulo_eliminar,
                                              text="                                                         ",
                                              background="black", font=("Candara", 30))
        self.label_vacio_eliminar2 = tk.Label(self.frame_titulo_eliminar,
                                               text="                                                         ",
                                               background="black", font=("Candara", 30))
        self.label_vacio_eliminar.grid(row=0, column=0)
        self.label_vacio_eliminar2.grid(row=0, column=2)

        self.cedula_eliminar = tk.Label(self.frame_botones_eliminar)
        self.cedula_eliminar.config(font=("Candara", 48), fg="white", background="black",
                                     image=self.imagen_boton_registrar_cedula)
        self.cedula_eliminar.grid(row=2, column=0)
        self.entrada_cedula = tk.Entry(self.frame_botones_eliminar, font="Candara", bd=4, width=30, justify="center")
        self.entrada_cedula.grid(row=2, column=1)
        self.boton_eliminar_usuario=tk.Button(self.frame_botones_eliminar,borderwidth=0,image=self.imagen_boton_eliminar_eliminar,background="black",command=self.eliminar_usuario)
        self.boton_eliminar_usuario.grid(row=3,column=1)

        self.boton_devolverse = tk.Button(self.frame_botones_eliminar, borderwidth=0,
                                          image=self.imagen_boton_volver_menu_registrar, background="black",
                                          command=self.devolverse_eliminar_a_menu)
        self.boton_devolverse.grid(row=3, column=0)

        self.ventana_eliminar.mainloop()

    def eliminar_usuario(self):
        try:
            cedula=str(self.entrada_cedula.get())
            informacion.agregar_informacion_eliminar(cedula)
            hay_paciente=False
            if cedula.isdigit() is False:
                raise Exception("La cedula es un numero, ingresa el numero nuevamente.")

            for paciente in Paciente.lista_pacientes:
             if paciente.cedula ==cedula:
                Paciente.lista_pacientes.remove(paciente)
                tk.messagebox.showinfo("Eliminación", " la eliminación del usuario se hizo sin problemas.")
                self.ventana_eliminar.destroy()
                self.window.iconify()
                self.window.state("zoomed")
                hay_paciente=True
            if hay_paciente is False:
                raise Exception("No se encuentra el paciente")
        except Exception as error:
            tk.messagebox.showwarning("Error",str(error))

    def registrar_cita(self):
        self.window.withdraw()
        self.ventana_registrar_cita=tk.Toplevel()
        self.ventana_registrar_cita.iconbitmap("imagenes/logo_ventana.ico")
        self.ventana_registrar_cita.geometry("1280x820")
        self.ventana_registrar_cita.title("Registrar cita")
        self.ventana_registrar_cita.resizable(False, False)
        self.ventana_registrar_cita.config(background="black")
        self.frame_titulo_registrar_cita=tk.Frame(self.ventana_registrar_cita)
        self.frame_titulo_registrar_cita.config(background="black")
        self.frame_titulo_registrar_cita.grid(row=0,column=1)
        self.frame_botones_registrar_cita=tk.Frame(self.ventana_registrar_cita)
        self.frame_botones_registrar_cita.config(background="black")
        self.frame_botones_registrar_cita.grid(row=1,column=1)

        self.frame_botones_padre_registrar_cita=tk.Frame(self.ventana_registrar_cita)
        self.frame_botones_padre_registrar_cita.config(background="black")
        self.frame_botones_padre_registrar_cita.grid(row=2,column=1)

        self.label_titulo_registrar_cita=tk.Label(self.frame_titulo_registrar_cita, text="Consultorio")
        self.label_titulo_registrar_cita.config(font=("Candara",48),fg="white", background="black",
                                    image=self.imagen_titulo_pequena)
        self.label_titulo_registrar_cita.grid(row=0,column=1)

        self.label_vacio_registrar_cita = tk.Label(self.frame_titulo_registrar_cita,
                                             text="                                                         ",
                                             background="black", font=("Candara", 30))
        self.label_vacio_registrar_cita2 = tk.Label(self.frame_titulo_registrar_cita,
                                              text="                                                         ",
                                              background="black", font=("Candara", 30))
        self.label_vacio_registrar_cita.grid(row=0, column=0)
        self.label_vacio_registrar_cita2.grid(row=0, column=2)

        self.cedula_registrar_cita = tk.Label(self.frame_botones_registrar_cita)
        self.cedula_registrar_cita.config(font=("Candara", 48), fg="white", background="black",
                                    image=self.imagen_boton_registrar_cedula)
        self.cedula_registrar_cita.grid(row=2, column=0)
        self.entrada_cedula_registrar_cita = tk.Entry(self.frame_botones_registrar_cita, font="Candara", bd=4, width=30, justify="center")
        self.entrada_cedula_registrar_cita.grid(row=2, column=1)



        self.fecha_registrar_cita = tk.Label(self.frame_botones_registrar_cita)
        self.fecha_registrar_cita.config(font=("Candara", 48), fg="white", background="black",
                                          image=self.imagen_label_fecha_registrar_cita)
        self.fecha_registrar_cita.grid(row=3, column=0)
        self.entrada_fecha_registrar_cita = tk.Entry(self.frame_botones_registrar_cita, font="Candara", bd=4, width=30,
                                                      justify="center")
        self.entrada_fecha_registrar_cita.grid(row=3, column=1)

        self.hora_registrar_cita = tk.Label(self.frame_botones_registrar_cita)
        self.hora_registrar_cita.config(font=("Candara", 48), fg="white", background="black",
                                         image=self.imagen_label_hora_registrar_cita)
        self.hora_registrar_cita.grid(row=4, column=0)
        self.entrada_hora_registrar_cita = tk.Entry(self.frame_botones_registrar_cita, font="Candara", bd=4, width=30,
                                                     justify="center")
        self.entrada_hora_registrar_cita.grid(row=4, column=1)



        self.boton_obtener_info_registrar_cita = tk.Button(self.frame_botones_padre_registrar_cita, borderwidth=0,
                                            image=self.imagen_boton_registrar_cita, background="black",
                                            command=self.obtener_informacion_registrar_cita)
        self.boton_obtener_info_registrar_cita.grid(row=0, column=1)

        self.boton_devolverse_registrar_cita = tk.Button(self.frame_botones_padre_registrar_cita, borderwidth=0,
                                          image=self.imagen_boton_volver_menu_registrar, background="black",
                                          command=self.devolverse_registrar_cita_a_menu)
        self.boton_devolverse_registrar_cita.grid(row=0, column=0)

    def obtener_informacion_registrar_cita(self):
        try:
            cedula=self.entrada_cedula_registrar_cita.get()
            fecha=self.entrada_fecha_registrar_cita.get()
            hora=self.entrada_hora_registrar_cita.get()
            verificar_fecha = datetime.strptime(fecha, "%d/%m/%Y")
            verificar_hora= datetime.strptime(hora, "%H")
            if cedula.isdigit() is False:
                raise Exception("La cedula es un nùmero, ingresalo nuevamente")


            diccionario={"cedula":cedula,"fecha":fecha,"hora":hora}
            informacion.agregar_informacion_registrar_cita(diccionario)

            tk.messagebox.showinfo("Registro exitoso", "Se pudo registrar la cita exitosamente")
            self.ventana_registrar_cita.destroy()
            self.window.deiconify()
            self.window.state("zoomed")
        except ValueError as error:
            tk.messagebox.showwarning("Ingresa bien las fechas", str(error))

        except Exception as error:
            tk.messagebox.showwarning("Mala digitación", str(error))

























































































