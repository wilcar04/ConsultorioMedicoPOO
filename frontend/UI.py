import tkinter as tk
from backend.ModeloDelMundo import *
from tkinter import messagebox
from datetime import *
import os

info = Informacion()


class UI:
    TEXTO_H_L="""HISTORIA CLINICA 
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

"""
    TEXTO_E_M="""RESULTADO DE EXAMEN:

Nombre:
Edad :
Sexo :
Ocupación :
Previsión :
Domicilio :


TIPO DE EXAMEN:




OBSERVACIONES:"""
    def __init__(self, nombre: str):
        self.imagen_boton_atender_paciente = None
        self.boton_5 = None
        self.imagen_boton_cancelar_cita = None
        self.cedula_cancelar_cita = None
        self.label_vacio_cancelar_cita2 = None
        self.label_vacio_cancelar_cita = None
        self.label_cancelar_cita = None
        self.frame_botones_cancelar_cita = None
        self.frame_titulo_cancelar_cita = None
        self.ventana_cancelar_cita = None
        self.entry_cedula_cancelar_cita = None
        self.boton_cancelar_cita_usuario = None
        self.boton_return_cancelar_cita = None
        self.boton_return_confirmar_cita = None
        self.boton_return_registrar_cita = None
        self.boton_get_info_registrar_cita = None
        self.entrada_hora_registrar_cita = None
        self.hora_registrar_cita = None
        self.entrada_fecha_registrar_cita = None
        self.fecha_registrar_cita = None
        self.entrada_cedula_registrar_cita = None
        self.cedula_registrar_cita = None
        self.label_vacio_registrar_cita2 = None
        self.label_vacio_registrar_cita = None
        self.label_titulo_registrar_cita = None
        self.boton_4 = None
        self.frame_botones_padre_registrar_cita = None
        self.frame_botones_registrar_cita = None
        self.frame_titulo_registrar_cita = None
        self.ventana_registrar_cita = None
        self.boton_3 = None
        self.boton_2 = None
        self.boton_1 = None
        self.label_2 = None
        self.label_1 = None
        self.frame_botones = None
        self.label_vacio_2 = None
        self.label_vacio = None
        self.frame_titulo = None
        self.imagen_titulo_pequena = None
        self.imagen_titulo = None
        self.imagen_boton_confirmar_cita = None
        self.imagen_label_hora_registrar_cita = None
        self.imagen_label_fecha_registrar_cita = None
        self.imagen_boton_volver_menu_registrar = None
        self.imagen_boton_registrar_celular = None
        self.imagen_boton_registrar_fecha = None
        self.imagen_boton_registrar_sexo = None
        self.imagen_boton_registrar_cedula = None
        self.imagen_boton_registrar_cita = None
        self.imagen_boton_eliminar_eliminar = None
        self.imagen_boton_registrar_registrar = None
        self.imagen_boton_registrar_nombre = None
        self.window = None
        self.entry_cedula_confirmar_cita = None
        self.label_vacio_confirmar_cita2 = None
        self.cedula_confirmar_cita = None
        self.label_vacio_confirmar_cita = None
        self.label_confirmar_cita = None
        self.frame_botones_confirmar_cita = None
        self.frame_titulo_confirmar_cita = None
        self.ventana_confirmar_cita = None
        self.boton_eliminar_user = None
        self.cedula_eliminar = None
        self.label_vacio_eliminar2 = None
        self.label_vacio_eliminar = None
        self.label_delete = None
        self.frame_buttons_delete = None
        self.frame_title_delete = None
        self.ventana_delete = None
        self.button_return = None
        self.button_get_info = None
        self.entry_cell = None
        self.cell_registrar = None
        self.entry_date = None
        self.date_registrar = None
        self.entry_gender = None
        self.gender_registrar = None
        self.frame_button_padre_registrar = None
        self.frame_buttons_registrar = None
        self.frame_title_registrar = None
        self.entry_id = None
        self.id_registrar = None
        self.entry_name = None
        self.name_registrar = None
        self.label_registrar = None
        self.label_empty_registrar2 = None
        self.label_empty_registrar = None
        self.ventana_registrar = None
        self.boton_confirmar_cita_usuario = None
        self.nombre = nombre

    def create_ventana_principal(self):
        self.window = tk.Tk()
        self.window.iconbitmap("images/logo_ventana.ico")
        self.window.geometry("1280x720")
        self.window.resizable(True, True)
        self.window.title("Consultorio")
        self.window.config(background="black")
        self.window.maxsize(1280, 720)

        # Load imagen

        self.imagen_titulo = tk.PhotoImage(file="images/logo_titulo.png")
        self.imagen_boton_registrar_nombre = tk.PhotoImage(file="images/btn_nombre_registrar.png")
        self.imagen_boton_registrar_registrar = tk.PhotoImage(file="images/btn_registrar_registrar.png")
        self.imagen_boton_eliminar_eliminar = tk.PhotoImage(file="images/lbl_eliminar_eliminar_usuario.png")
        self.imagen_boton_registrar_cita = tk.PhotoImage(file="images/btn_registrar_cita.png")

        self.imagen_boton_registrar_cedula = tk.PhotoImage(file="images/btn_cedula_registrar.png")
        self.imagen_boton_registrar_sexo = tk.PhotoImage(file="images/btn_sexo_registrar.png")
        self.imagen_boton_registrar_fecha = tk.PhotoImage(file="images/btn_fecha_registrar.png")
        self.imagen_boton_registrar_celular = tk.PhotoImage(file="images/btn_registrar_celular.png")
        self.imagen_boton_volver_menu_registrar = tk.PhotoImage(file="images/btn_registrar_volver_menu.png")
        self.imagen_label_fecha_registrar_cita = tk.PhotoImage(file="images/lbl_fecha_registrar_cita.png")
        self.imagen_label_hora_registrar_cita = tk.PhotoImage(file="images/lbl_hora_registrar_cita.png")
        self.imagen_boton_confirmar_cita = tk.PhotoImage(file="images/btn_confirmar_cita.png")
        self.imagen_boton_cancelar_cita = tk.PhotoImage(file="images/btn_cancelar_cita.png")
        self.imagen_boton_atender_paciente = tk.PhotoImage(file="images/btn_atender_paciente.png")
        self.imagen_boton_historia_medica= tk.PhotoImage(file="images/btn_historia_medica.png")
        self.imagen_boton_resultados_examenes= tk.PhotoImage(file="images/btn_resultados_examen.png")
        self.imagen_boton_obtener_citas_pendientes= tk.PhotoImage(file="images/btn_citas_pendientes.png")
        self.imagen_boton_historial_paciente= tk.PhotoImage(file="images/btn_historial_paciente.png")

        self.imagen_titulo = self.imagen_titulo.subsample(2)
        self.imagen_titulo_pequena = self.imagen_titulo.subsample(2)

        # Frame Titulo
        self.frame_titulo = tk.Frame(self.window)
        self.frame_titulo.config(background="black")
        self.frame_titulo.grid(row=0, column=0)

        # Labels vacios para centrar Titulo
        self.label_vacio = tk.Label(self.frame_titulo, text="                                             ",
                                    background="black", font=("Candara", 30))
        self.label_vacio_2 = tk.Label(self.frame_titulo, text="                                             ",
                                      background="black", font=("Candara", 30))
        self.label_vacio.grid(row=0, column=0)
        self.label_vacio_2.grid(row=0, column=2)

        # Frame Botones
        self.frame_botones = tk.Frame(self.window)
        self.frame_botones.config(background="black")
        self.frame_botones.grid(row=1, column=0)

        # Titulo -> Logo
        self.label_1 = tk.Label(self.frame_titulo, text="Consultorio")
        self.label_1.config(font=("Candara", 48), fg="white", background="black", image=self.imagen_titulo)
        self.label_1.grid(row=0, column=1)

        # Texto respuesta para cuando se registra
        self.label_2 = tk.Label(self.frame_botones)

        self.label_2.config(font="Candara", fg="white", background="black")

        self.boton_1 = tk.Button(self.frame_botones, text="Registrar Usuario", borderwidth=0,
                                 image=self.imagen_boton_registrar_registrar, command=self.registrar)
        self.boton_1.config(font="Candara", fg="white", background="black")
        self.boton_2 = tk.Button(self.frame_botones, text="Elimino Usuario", command=self.delete, borderwidth=0,
                                 image=self.imagen_boton_eliminar_eliminar)
        self.boton_2.config(font="Candara", fg="white", background="black")
        self.boton_3 = tk.Button(self.frame_botones, text="Registrar Cita", borderwidth=0,
                                 image=self.imagen_boton_registrar_cita, command=self.registrar_medical_appointment)
        self.boton_3.config(font="Candara", fg="white", background="black")
        self.boton_4 = tk.Button(self.frame_botones, text="Confirmar cita", borderwidth=0,
                                 image=self.imagen_boton_confirmar_cita, command=self.confirm_medical_appointment)
        self.boton_4.config(font="Candara", fg="white", background="black")
        self.boton_5 = tk.Button(self.frame_botones, text="Cancelar Cita", borderwidth=0,
                                 image=self.imagen_boton_cancelar_cita, command=self.delete_medical_appointment)
        self.boton_5.config(font="Candara", fg="white", background="black")
        self.boton_6 = tk.Button(self.frame_botones, text="Atender Cita", borderwidth=0,
                                 image=self.imagen_boton_atender_paciente, command=self.atender_cita_medica)
        self.boton_6.config(font="Candara", fg="white", background="black")
        self.boton_7 =tk.Button(self.frame_botones,text="Citas Pendientes", borderwidth=0,
                                image=self.imagen_boton_obtener_citas_pendientes,command=self.obtener_la_agenda_de_las_citas_pendientes)
        self.boton_7.config(font="Candara",fg="white",background="black")
        self.boton_8 = tk.Button(self.frame_botones,image=self.imagen_boton_historial_paciente,command=self.historial_paciente,borderwidth=0)
        self.boton_8.config(fg="white",background="black")



        # Empaquetar los Botones
        self.boton_1.grid(row=0, column=0)
        self.boton_2.grid(row=0, column=1)
        self.boton_3.grid(row=0, column=2)
        self.boton_4.grid(row=1, column=0)
        self.boton_5.grid(row=1, column=1)
        self.boton_6.grid(row=1, column=2)
        self.boton_7.grid(row=2, column=0)
        self.boton_8.grid(row=2,column=1)


        self.window.mainloop()

    def registrar(self):
        self.window.withdraw()
        self.ventana_registrar = tk.Toplevel()
        self.ventana_registrar.maxsize(1280, 820)
        self.ventana_registrar.state("zoomed")
        self.ventana_registrar.iconbitmap("images/logo_ventana.ico")
        self.ventana_registrar.geometry("1280x820")
        self.ventana_registrar.title("Registrar")
        self.ventana_registrar.resizable(True, True)
        self.ventana_registrar.config(background="black")
        self.frame_title_registrar = tk.Frame(self.ventana_registrar)
        self.frame_buttons_registrar = tk.Frame(self.ventana_registrar)
        self.frame_button_padre_registrar = tk.Frame(self.ventana_registrar)
        self.frame_buttons_registrar.config(background="black")
        self.frame_title_registrar.config(background="black")
        self.frame_button_padre_registrar.config(background="black")
        self.frame_title_registrar.grid(row=0, column=0)
        self.frame_buttons_registrar.grid(row=1, column=0)
        self.frame_button_padre_registrar.grid(row=2, column=0)

        self.label_empty_registrar = tk.Label(self.frame_title_registrar,
                                              text="                                                         ",
                                              background="black", font=("Candara", 30))
        self.label_empty_registrar2 = tk.Label(self.frame_title_registrar,
                                               text="                                                         ",
                                               background="black", font=("Candara", 30))
        self.label_empty_registrar.grid(row=0, column=0)
        self.label_empty_registrar2.grid(row=0, column=2)

        # Titular -> Logo
        self.label_registrar = tk.Label(self.frame_title_registrar, text="doctor's office")
        self.label_registrar.config(font=("Candara", 48), fg="white", background="black",
                                    image=self.imagen_titulo_pequena)
        self.label_registrar.grid(row=0, column=1)
        # input -> info
        self.name_registrar = tk.Label(self.frame_buttons_registrar)
        self.name_registrar.config(font=("Candara", 48), fg="white", background="black",
                                   image=self.imagen_boton_registrar_nombre)
        self.name_registrar.grid(row=2, column=0)
        self.entry_name = tk.Entry(self.frame_buttons_registrar, font=("Arial rounded MT", 14), bd=4, width=30, justify="center")
        self.entry_name.grid(row=2, column=1)

        self.id_registrar = tk.Label(self.frame_buttons_registrar)
        self.id_registrar.config(font=("Candara", 48), fg="white", background="black",
                                 image=self.imagen_boton_registrar_cedula)
        self.id_registrar.grid(row=3, column=0)
        self.entry_id = tk.Entry(self.frame_buttons_registrar, font=("Arial rounded MT", 14), bd=4, width=30, justify="center")
        self.entry_id.grid(row=3, column=1)

        self.gender_registrar = tk.Label(self.frame_buttons_registrar)
        self.gender_registrar.config(font=("Candara", 48), fg="white", background="black",
                                     image=self.imagen_boton_registrar_sexo)
        self.gender_registrar.grid(row=4, column=0)
        self.entry_gender = tk.Entry(self.frame_buttons_registrar, font=("Arial rounded MT", 14), bd=4, width=30, justify="center")
        self.entry_gender.grid(row=4, column=1)

        self.date_registrar = tk.Label(self.frame_buttons_registrar)
        self.date_registrar.config(font=("Candara", 48), fg="white", background="black",
                                   image=self.imagen_boton_registrar_fecha)
        self.date_registrar.grid(row=5, column=0)
        self.entry_date = tk.Entry(self.frame_buttons_registrar, font=("Arial rounded MT", 14), bd=4, width=30, justify="center")
        self.entry_date.grid(row=5, column=1)

        self.cell_registrar = tk.Label(self.frame_buttons_registrar)
        self.cell_registrar.config(font=("Candara", 48), fg="white", background="black",
                                   image=self.imagen_boton_registrar_celular)
        self.cell_registrar.grid(row=6, column=0)
        self.entry_cell = tk.Entry(self.frame_buttons_registrar, font=("Arial rounded MT", 14), bd=4, width=30, justify="center")
        self.entry_cell.grid(row=6, column=1)

        self.button_get_info = tk.Button(self.frame_button_padre_registrar, borderwidth=0,
                                         image=self.imagen_boton_registrar_registrar, background="black",
                                         command=self.get_info)
        self.button_get_info.grid(row=0, column=1)

        self.button_return = tk.Button(self.frame_button_padre_registrar, borderwidth=0,
                                       image=self.imagen_boton_volver_menu_registrar, background="black",
                                       command=self.return_registrar_a_menu)
        self.button_return.grid(row=0, column=0)

        self.ventana_registrar.mainloop()

    def get_info(self):
        try:
            name = self.entry_name.get()
            id_get_info = self.entry_id.get()
            gender = self.entry_gender.get()
            date_get_info = self.entry_date.get()
            cel_get_info = self.entry_cell.get()
            name = name.replace(" ", "")
            test_name = name.isalpha()
            test_id = id_get_info.isdigit()
            test_date = datetime.strptime(date_get_info, "%d/%m/%Y")

            test_gender = gender.isalpha()
            test_cell = cel_get_info.isdigit()

            if not test_name:
                raise Exception("No ingresaste el nombre correctamente.")
            if test_id is False and len(id_get_info) <= 10:
                raise Exception("No ingresaste bien la cedula.")
            if test_gender is False:
                raise Exception("No ingresaste bien el genero.")
            if test_cell is False:
                raise Exception("No ingresaste bien el teléfono")

            if test_date == datetime.strptime(date_get_info, "%d/%m/%Y"):
                pass

        except ValueError as error:
            tk.messagebox.showwarning("wrong data entry", str(error))
        except Exception as error:
            tk.messagebox.showwarning("wrong data entry", f"{str(error)}")
        else:
            dictionary = {"name": name, "id": id_get_info, "gender": gender, "date": date_get_info,
                          "cel_get_info": cel_get_info}
            tk.messagebox.showinfo("Registro", " El registro se hizo sin problemas")
            info.agregar_informacion_registrar(dictionary)
            print(info.informacion_registrar)
            self.ventana_registrar.destroy()
            self.window.iconify()
            self.window.state("zoomed")



    def delete(self):
        self.window.withdraw()
        self.ventana_delete = tk.Toplevel()
        self.ventana_delete.maxsize(1280, 420)
        self.ventana_delete.state("zoomed")
        self.ventana_delete.iconbitmap("images/logo_ventana.ico")
        self.ventana_delete.geometry("720x420")
        self.ventana_delete.title("Eliminar")
        self.ventana_delete.resizable(True, True)
        self.ventana_delete.config(background="black")

        self.frame_title_delete = tk.Frame(self.ventana_delete)
        self.frame_title_delete.config(background="black")
        self.frame_buttons_delete = tk.Frame(self.ventana_delete)
        self.frame_buttons_delete.config(background="black")
        self.frame_title_delete.grid(row=0, column=1)
        self.frame_buttons_delete.grid(row=1, column=1)

        self.label_delete = tk.Label(self.frame_title_delete, text="Consultorio")
        self.label_delete.config(font=("Candara", 48), fg="white", background="black",
                                 image=self.imagen_titulo_pequena)
        self.label_delete.grid(row=0, column=1)

        self.label_vacio_eliminar = tk.Label(self.frame_title_delete,
                                             text="                                                         ",
                                             background="black", font=("Candara", 30))
        self.label_vacio_eliminar2 = tk.Label(self.frame_title_delete,
                                              text="                                                         ",
                                              background="black", font=("Candara", 30))
        self.label_vacio_eliminar.grid(row=0, column=0)
        self.label_vacio_eliminar2.grid(row=0, column=2)

        self.cedula_eliminar = tk.Label(self.frame_buttons_delete)
        self.cedula_eliminar.config(font=("Candara", 48), fg="white", background="black",
                                    image=self.imagen_boton_registrar_cedula)
        self.cedula_eliminar.grid(row=2, column=0)
        self.entry_id = tk.Entry(self.frame_buttons_delete, font=("Arial rounded MT", 18), bd=4, width=30, justify="center")
        self.entry_id.grid(row=2, column=1)
        self.boton_eliminar_user = tk.Button(self.frame_buttons_delete, borderwidth=0,
                                             image=self.imagen_boton_eliminar_eliminar, background="black",
                                             command=self.delete_user)
        self.boton_eliminar_user.grid(row=3, column=1)

        self.button_return = tk.Button(self.frame_buttons_delete, borderwidth=0,
                                       image=self.imagen_boton_volver_menu_registrar, background="black",
                                       command=self.return_delete_a_menu)
        self.button_return.grid(row=3, column=0)

        self.ventana_delete.mainloop()

    def delete_user(self):
        try:
            cedula = str(self.entry_id.get())
            hay_patient = True  # Este valor se cambia en el backend para la excepcion ("No se encuentra paciente")
            if cedula.isdigit() is False:
                raise Exception("La cedula es un numero, ingresa el numero nuevamente.")

            if hay_patient is False:
                raise Exception("No se encuentra el paciente")
        except Exception as error:
            tk.messagebox.showwarning("Error", str(error))
        else:
            info.agregar_informacion_eliminar(cedula)
            print(info.informacion_eliminar)
            tk.messagebox.showinfo("Eliminación", " la eliminación del usuario se hizo sin problemas.")
            self.ventana_delete.destroy()
            self.window.iconify()
            self.window.state("zoomed")

    def registrar_medical_appointment(self):
        self.window.withdraw()
        self.ventana_registrar_cita = tk.Toplevel()
        self.ventana_registrar_cita.maxsize(1280, 720)
        self.ventana_registrar_cita.state("zoomed")
        self.ventana_registrar_cita.iconbitmap("images/logo_ventana.ico")
        self.ventana_registrar_cita.geometry("1280x820")
        self.ventana_registrar_cita.title("Registrar cita")
        self.ventana_registrar_cita.resizable(True, True)
        self.ventana_registrar_cita.config(background="black")
        self.frame_titulo_registrar_cita = tk.Frame(self.ventana_registrar_cita)
        self.frame_titulo_registrar_cita.config(background="black")
        self.frame_titulo_registrar_cita.grid(row=0, column=1)
        self.frame_botones_registrar_cita = tk.Frame(self.ventana_registrar_cita)
        self.frame_botones_registrar_cita.config(background="black")
        self.frame_botones_registrar_cita.grid(row=1, column=1)

        self.frame_botones_padre_registrar_cita = tk.Frame(self.ventana_registrar_cita)
        self.frame_botones_padre_registrar_cita.config(background="black")
        self.frame_botones_padre_registrar_cita.grid(row=2, column=1)

        self.label_titulo_registrar_cita = tk.Label(self.frame_titulo_registrar_cita, text="Consultorio")
        self.label_titulo_registrar_cita.config(font=("Candara", 48), fg="white", background="black",
                                                image=self.imagen_titulo_pequena)
        self.label_titulo_registrar_cita.grid(row=0, column=1)

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
        self.entrada_cedula_registrar_cita = tk.Entry(self.frame_botones_registrar_cita, font=("Arial rounded MT", 18), bd=4, width=30,
                                                      justify="center")
        self.entrada_cedula_registrar_cita.grid(row=2, column=1)

        self.fecha_registrar_cita = tk.Label(self.frame_botones_registrar_cita)
        self.fecha_registrar_cita.config(font=("Candara", 48), fg="white", background="black",
                                         image=self.imagen_label_fecha_registrar_cita)
        self.fecha_registrar_cita.grid(row=3, column=0)
        self.entrada_fecha_registrar_cita = tk.Entry(self.frame_botones_registrar_cita, font=("Arial rounded MT", 18), bd=4, width=30,
                                                     justify="center")
        self.entrada_fecha_registrar_cita.grid(row=3, column=1)

        self.hora_registrar_cita = tk.Label(self.frame_botones_registrar_cita)
        self.hora_registrar_cita.config(font=("Candara", 48), fg="white", background="black",
                                        image=self.imagen_label_hora_registrar_cita)
        self.hora_registrar_cita.grid(row=4, column=0)
        self.entrada_hora_registrar_cita = tk.Entry(self.frame_botones_registrar_cita, font=("Arial rounded MT", 18), bd=4, width=30,
                                                    justify="center")
        self.entrada_hora_registrar_cita.grid(row=4, column=1)

        self.boton_get_info_registrar_cita = tk.Button(self.frame_botones_padre_registrar_cita, borderwidth=0,
                                                       image=self.imagen_boton_registrar_cita, background="black",
                                                       command=self.get_info_registrar_medical_appointment)
        self.boton_get_info_registrar_cita.grid(row=0, column=1)

        self.boton_return_registrar_cita = tk.Button(self.frame_botones_padre_registrar_cita, borderwidth=0,
                                                     image=self.imagen_boton_volver_menu_registrar,
                                                     background="black",
                                                     command=self.return_registrar_medical_appointment_a_menu)
        self.boton_return_registrar_cita.grid(row=0, column=0)

    def get_info_registrar_medical_appointment(self):
        try:
            cedula = self.entrada_cedula_registrar_cita.get()
            fecha = self.entrada_fecha_registrar_cita.get()
            hora = self.entrada_hora_registrar_cita.get()
            verificar_fecha = datetime.strptime(fecha, "%d/%m/%Y")
            verificar_hora = datetime.strptime(hora, "%H")
            hay_paciente = True
            if cedula.isdigit() is False:
                raise Exception("La cedula es un nùmero, ingresalo nuevamente")
            if hay_paciente is False:
                raise Exception("El paciente no esta registrado")
            if verificar_fecha == datetime.strptime(fecha, "%d/%m/%Y"):
                pass
            if verificar_hora == datetime.strptime(hora, "%H"):
                pass

        except ValueError as error:
            tk.messagebox.showwarning("Ingresa bien la fecha", str(error))

        except Exception as error:
            tk.messagebox.showwarning("error", str(error))
        else:
            diccionario = {"cedula": cedula, "fecha": fecha, "hora": hora}
            tk.messagebox.showinfo("Registro exitoso", "Se pudo registrar la cita exitosamente")
            info.agregar_informacion_registrar_cita(diccionario)
            print(info.informacion_registrar_cita)
            self.ventana_registrar_cita.destroy()
            self.window.deiconify()
            self.window.state("zoomed")

    def confirm_medical_appointment(self):
        self.window.withdraw()

        self.ventana_confirmar_cita = tk.Toplevel()
        self.ventana_confirmar_cita.maxsize(1280, 720)
        self.ventana_confirmar_cita.state("zoomed")
        self.ventana_confirmar_cita.iconbitmap("images/logo_ventana.ico")
        self.ventana_confirmar_cita.geometry("1280x420")
        self.ventana_confirmar_cita.title("Confirmar_cita")
        self.ventana_confirmar_cita.resizable(True, True)
        self.ventana_confirmar_cita.config(background="black")

        self.frame_titulo_confirmar_cita = tk.Frame(self.ventana_confirmar_cita)
        self.frame_titulo_confirmar_cita.config(background="black")
        self.frame_botones_confirmar_cita = tk.Frame(self.ventana_confirmar_cita)
        self.frame_botones_confirmar_cita.config(background="black")
        self.frame_titulo_confirmar_cita.grid(row=0, column=1)
        self.frame_botones_confirmar_cita.grid(row=1, column=1)

        self.label_confirmar_cita = tk.Label(self.frame_titulo_confirmar_cita, text="Consultorio")
        self.label_confirmar_cita.config(font=("Candara", 48), fg="white", background="black",
                                         image=self.imagen_titulo_pequena)
        self.label_confirmar_cita.grid(row=0, column=1)

        self.label_vacio_confirmar_cita = tk.Label(self.frame_titulo_confirmar_cita,
                                                   text="                                                         ",
                                                   background="black", font=("Candara", 30))
        self.label_vacio_confirmar_cita2 = tk.Label(self.frame_titulo_confirmar_cita,
                                                    text="                                                         ",
                                                    background="black", font=("Candara", 30))
        self.label_vacio_confirmar_cita.grid(row=0, column=0)
        self.label_vacio_confirmar_cita2.grid(row=0, column=2)

        self.cedula_confirmar_cita = tk.Label(self.frame_botones_confirmar_cita)
        self.cedula_confirmar_cita.config(font=("Candara", 48), fg="white", background="black",
                                          image=self.imagen_boton_registrar_cedula)
        self.cedula_confirmar_cita.grid(row=2, column=0)
        self.entry_cedula_confirmar_cita = tk.Entry(self.frame_botones_confirmar_cita, font=("Arial rounded MT", 18), bd=4, width=30,
                                                    justify="center")
        self.entry_cedula_confirmar_cita.grid(row=2, column=1)
        self.boton_confirmar_cita_usuario = tk.Button(self.frame_botones_confirmar_cita, borderwidth=0,
                                                      image=self.imagen_boton_confirmar_cita, background="black",
                                                      command=self.get_info_confirmar_cita)
        self.boton_confirmar_cita_usuario.grid(row=3, column=1)

        self.boton_return_confirmar_cita = tk.Button(self.frame_botones_confirmar_cita, borderwidth=0,
                                                     image=self.imagen_boton_volver_menu_registrar,
                                                     background="black",
                                                     command=self.return_confirm_medical_appointment_a_menu)
        self.boton_return_confirmar_cita.grid(row=3, column=0)

        self.ventana_confirmar_cita.mainloop()

    def get_info_confirmar_cita(self):
        try:
            cedula = str(self.entry_cedula_confirmar_cita.get())
            hay_paciente = True
            have_medical_appointment = True

            if cedula.isdigit() is False:
                raise Exception("La cedula es un numero, ingresa el numero nuevamente.")

            if hay_paciente is False:
                raise Exception("No se encuentra el paciente")

            if have_medical_appointment is False:
                raise Exception("El paciente no tiene una cita asignada")

        except Exception as error:
            tk.messagebox.showwarning("Error", str(error))

        else:
            info.agregar_informacion_confirmar_cita(cedula)
            print(info.informacion_confirmar_cita)
            tk.messagebox.showinfo("Confirmación", " la confirmación de la cita se hizo sin problemas.")
            self.ventana_confirmar_cita.destroy()
            self.window.iconify()
            self.window.state("zoomed")

    def delete_medical_appointment(self):
        self.window.withdraw()

        self.ventana_cancelar_cita = tk.Toplevel()
        self.ventana_cancelar_cita.maxsize(1280, 720)
        self.ventana_cancelar_cita.state("zoomed")
        self.ventana_cancelar_cita.iconbitmap("images/logo_ventana.ico")
        self.ventana_cancelar_cita.geometry("1280x420")
        self.ventana_cancelar_cita.title("Cancelar Cita")
        self.ventana_cancelar_cita.resizable(True, True)
        self.ventana_cancelar_cita.config(background="black")

        self.frame_titulo_cancelar_cita = tk.Frame(self.ventana_cancelar_cita)
        self.frame_titulo_cancelar_cita.config(background="black")
        self.frame_botones_cancelar_cita = tk.Frame(self.ventana_cancelar_cita)
        self.frame_botones_cancelar_cita.config(background="black")
        self.frame_titulo_cancelar_cita.grid(row=0, column=1)
        self.frame_botones_cancelar_cita.grid(row=1, column=1)

        self.label_cancelar_cita = tk.Label(self.frame_titulo_cancelar_cita, text="Consultorio")
        self.label_cancelar_cita.config(font=("Candara", 48), fg="white", background="black",
                                        image=self.imagen_titulo_pequena)
        self.label_cancelar_cita.grid(row=0, column=1)

        self.label_vacio_cancelar_cita = tk.Label(self.frame_titulo_cancelar_cita,
                                                  text="                                                         ",
                                                  background="black", font=("Candara", 30))
        self.label_vacio_cancelar_cita2 = tk.Label(self.frame_titulo_cancelar_cita,
                                                   text="                                                         ",
                                                   background="black", font=("Candara", 30))
        self.label_vacio_cancelar_cita.grid(row=0, column=0)
        self.label_vacio_cancelar_cita2.grid(row=0, column=2)

        self.cedula_cancelar_cita = tk.Label(self.frame_botones_cancelar_cita)
        self.cedula_cancelar_cita.config(font=("Candara", 48), fg="white", background="black",
                                         image=self.imagen_boton_registrar_cedula)
        self.cedula_cancelar_cita.grid(row=2, column=0)
        self.entry_cedula_cancelar_cita = tk.Entry(self.frame_botones_cancelar_cita, font=("Arial rounded MT", 18), bd=4, width=30,
                                                   justify="center")
        self.entry_cedula_cancelar_cita.grid(row=2, column=1)
        self.boton_cancelar_cita_usuario = tk.Button(self.frame_botones_cancelar_cita, borderwidth=0,
                                                     image=self.imagen_boton_cancelar_cita, background="black",
                                                     command=self.get_info_cancelar_cita)
        self.boton_cancelar_cita_usuario.grid(row=3, column=1)

        self.boton_return_cancelar_cita = tk.Button(self.frame_botones_cancelar_cita, borderwidth=0,
                                                    image=self.imagen_boton_volver_menu_registrar,
                                                    background="black",
                                                    command=self.return_cancel_medical_appointment_a_menu)
        self.boton_return_cancelar_cita.grid(row=3, column=0)

        self.ventana_cancelar_cita.mainloop()

    def get_info_cancelar_cita(self):
        try:
            cedula = str(self.entry_cedula_cancelar_cita.get())
            hay_paciente = True
            have_medical_appointment = True

            if cedula.isdigit() is False:
                raise Exception("La cedula es un numero, ingresa el numero nuevamente.")

            if hay_paciente is False:
                raise Exception("No se encuentra el paciente")

            if have_medical_appointment is False:
                raise Exception("El paciente no tiene una cita asignada")

        except Exception as error:
            tk.messagebox.showwarning("Error", str(error))

        else:
            info.agregar_informacion_cancelar_cita(cedula)
            print(info.informacion_eliminar_cita)
            tk.messagebox.showinfo("Cancelación", " la eliminación de la cita se hizo sin problemas.")
            self.ventana_cancelar_cita.destroy()
            self.window.iconify()
            self.window.state("zoomed")

    def atender_cita_medica(self):
        self.window.withdraw()

        self.ventana_atender_cita = tk.Toplevel()
        self.ventana_atender_cita.maxsize(1280, 720)
        self.ventana_atender_cita.state("zoomed")
        self.ventana_atender_cita.iconbitmap("images/logo_ventana.ico")
        self.ventana_atender_cita.geometry("1280x420")
        self.ventana_atender_cita.title("Atender cita")
        self.ventana_atender_cita.resizable(True, True)
        self.ventana_atender_cita.config(background="black")

        self.frame_titulo_atender_cita = tk.Frame(self.ventana_atender_cita)
        self.frame_titulo_atender_cita.config(background="black")
        self.frame_botones_atender_cita = tk.Frame(self.ventana_atender_cita)
        self.frame_botones_atender_cita.config(background="black")
        self.frame_titulo_atender_cita.grid(row=0, column=1)
        self.frame_botones_atender_cita.grid(row=1, column=1)

        self.label_atender_cita = tk.Label(self.frame_titulo_atender_cita, text="Consultorio")
        self.label_atender_cita.config(font=("Candara", 48), fg="white", background="black",
                                       image=self.imagen_titulo_pequena)
        self.label_atender_cita.grid(row=0, column=1)

        self.label_vacio_atender_cita = tk.Label(self.frame_titulo_atender_cita,
                                                 text="                                                         ",
                                                 background="black", font=("Candara", 30))
        self.label_vacio_atender_cita2 = tk.Label(self.frame_titulo_atender_cita,
                                                  text="                                                         ",
                                                  background="black", font=("Candara", 30))
        self.label_vacio_atender_cita.grid(row=0, column=0)
        self.label_vacio_atender_cita2.grid(row=0, column=2)

        self.cedula_atender_cita = tk.Label(self.frame_botones_atender_cita)
        self.cedula_atender_cita.config(font=("Candara", 48), fg="white", background="black",
                                        image=self.imagen_boton_registrar_cedula)
        self.cedula_atender_cita.grid(row=2, column=0)
        self.entry_cedula_atender_cita = tk.Entry(self.frame_botones_atender_cita, font=("Arial rounded MT", 18), bd=4, width=30,
                                                  justify="center")
        self.entry_cedula_atender_cita.grid(row=2, column=1)
        self.boton_atender_cita_usuario = tk.Button(self.frame_botones_atender_cita, borderwidth=0,
                                                    image=self.imagen_boton_atender_paciente, background="black",
                                                    command=self.get_info_atender_cita)
        self.boton_atender_cita_usuario.grid(row=3, column=1)

        self.boton_return_atender_cita = tk.Button(self.frame_botones_atender_cita, borderwidth=0,
                                                   image=self.imagen_boton_volver_menu_registrar,
                                                   background="black",
                                                   command=self.return_atender_medical_appointment_a_menu)
        self.boton_return_atender_cita.grid(row=3, column=0)

        self.ventana_atender_cita.mainloop()

    def get_info_atender_cita(self):
        try:
            cedula = str(self.entry_cedula_atender_cita.get())
            hay_paciente = True
            have_medical_appointment = True

            if cedula.isdigit() is False:
                raise Exception("La cedula es un numero, ingresa el numero nuevamente.")

            if hay_paciente is False:
                raise Exception("No se encuentra el paciente")

            if have_medical_appointment is False:
                raise Exception("El paciente no tiene una cita asignada")

        except Exception as error:
            tk.messagebox.showwarning("Error", str(error))

        else:
            self.ventana_atender_cita.withdraw()
            self.ventana_elegir = tk.Toplevel()

            self.ventana_elegir.maxsize(1280, 720)
            self.ventana_elegir.state("zoomed")
            self.ventana_elegir.iconbitmap("images/logo_ventana.ico")
            self.ventana_elegir.geometry("720x420")
            self.ventana_elegir.title("Elegir Tipo de examen")
            self.ventana_elegir.resizable(True, True)
            self.ventana_elegir.config(background="black")

            self.frame_titulo_elegir = tk.Frame(self.ventana_elegir)
            self.frame_titulo_elegir.config(background="black")
            self.frame_titulo_elegir.grid(row=0, column=1)
            self.frame_botones_elegir = tk.Frame(self.ventana_elegir)
            self.frame_botones_elegir.config(background="black")
            self.frame_botones_elegir.grid(row=1,column=1)

            self.label_elegir = tk.Label(self.frame_titulo_elegir, text="Consultorio")
            self.label_elegir.config(font=("Candara", 48), fg="white", background="black",
                                     image=self.imagen_titulo_pequena)
            self.label_elegir.grid(row=0, column=1)

            self.label_vacio_elegir = tk.Label(self.frame_titulo_elegir,
                                               text="                                                         ",
                                               background="black", font=("Candara", 30))
            self.label_vacio_elegir2 = tk.Label(self.frame_titulo_elegir,
                                                text="                                                         ",
                                                background="black", font=("Candara", 30))
            self.label_vacio_elegir.grid(row=0, column=0)
            self.label_vacio_elegir2.grid(row=0, column=2)

            self.boton_historia_medica=tk.Button(self.frame_botones_elegir, borderwidth=0,
                                                    image=self.imagen_boton_historia_medica, background="black",
                                                    command=self.proceso_historia_medica)
            self.boton_resultado_examen=tk.Button(self.frame_botones_elegir, borderwidth=0, image=self.imagen_boton_resultados_examenes, background="black"
                                                  ,command=self.proceso_resultado_examen)

            self.boton_return_atender_cita = tk.Button(self.frame_botones_elegir, borderwidth=0,
                                                           image=self.imagen_boton_volver_menu_registrar,
                                                           background="black",
                                                           command=self.return_elegir_a_menu)

            self.boton_return_atender_cita.grid(row=3,column=2)
            self.boton_historia_medica.grid(row=3,column=0)
            self.boton_resultado_examen.grid(row=3,column=1)

            self.ventana_elegir.mainloop()


    def proceso_historia_medica(self):
        tk.messagebox.showinfo("Para el llenado de la historia medica del paciente", """
        1)  Se va abrir el editor de texto.
        2)  Editas el archivo y se guarda(Ctrl+S).
        3)  Aparece una ventana emergente de informacion, la cierras cuando ya hayas editado el archivo.""")

        os.startfile(r"C:\Users\jvald\PycharmProjects\Interfazz\frontend\files\historia_medica.txt")
        tk.messagebox.showinfo("Cierrame cuando hayas editado el archivo", "Cierrame cuando hayas editado el archivo")

        historia=open("files/historia_medica.txt","r",encoding="utf-8")
        texto_historia_medica = historia.read()
        historia.close()

        historia=open("files/historia_medica.txt", "w",encoding="utf-8")
        historia.write(UI.TEXTO_H_L)
        historia.close()
        diccionario={self.entry_cedula_atender_cita.get(): texto_historia_medica}
        info.informacion_historias_medicas.append(diccionario)
        print(info.informacion_historias_medicas)
        tk.messagebox.showinfo("Se ha ingresado correctamente",
                               "La información de los resultados de la historia medica se ingreso correctamente.")
        self.ventana_elegir.destroy()
        self.ventana_atender_cita.destroy()
        self.window.iconify()
        self.window.state("zoomed")


    def proceso_resultado_examen(self):
        tk.messagebox.showinfo("Para el llenado de los resultados de los examenes del paciente", """
                1)  Se va abrir el editor de texto.
                2)  Editas el archivo y se guarda(Ctrl+S).
                3)  Aparece una ventana emergente de informacion, la cierras cuando ya hallas editado el archivo.""")
        os.startfile(r"C:\Users\jvald\PycharmProjects\Interfazz\frontend\files\resultado_examen.txt")
        tk.messagebox.showinfo("Cierrame cuando hallas editado el archivo", "Cierrame cuando hayas editado el archivo")

        examen = open("files/resultado_examen.txt", "r", encoding="utf-8")
        texto_examen = examen.read()
        examen.close()
        examen= open("files/resultado_examen.txt", "w", encoding="utf-8")
        examen.write(UI.TEXTO_E_M)
        examen.close()


        diccionario = {self.entry_cedula_atender_cita.get(): texto_examen}
        info.informacion_resultados_examenes.append(diccionario)
        print(info.informacion_resultados_examenes)
        tk.messagebox.showinfo("Se ha ingresado correctamente", "La información de los resultados de los examenes medico se ingreso correctamente.")


        self.ventana_elegir.destroy()
        self.ventana_atender_cita.destroy()
        self.window.iconify()
        self.window.state("zoomed")

    def obtener_la_agenda_de_las_citas_pendientes(self):
        self.window.withdraw()
        self.ventana_citas_pendientes= tk.Toplevel()
        self.ventana_citas_pendientes.maxsize(1280, 820)
        self.ventana_citas_pendientes.state("zoomed")
        self.ventana_citas_pendientes.iconbitmap("images/logo_ventana.ico")
        self.ventana_citas_pendientes.geometry("1280x820")
        self.ventana_citas_pendientes.title("Agenda citas Pendientes")
        self.ventana_citas_pendientes.resizable(True, True)
        self.ventana_citas_pendientes.config(background="black")
        self.frame_title_citas_pendientes = tk.Frame(self.ventana_citas_pendientes)
        self.frame_title_citas_pendientes.config(background="black")
        self.frame_labels_citas_pendientes = tk.Frame(self.ventana_citas_pendientes)
        self.frame_labels_citas_pendientes.config(background="black")
        self.frame_title_citas_pendientes.grid(row=0,column=0)
        self.frame_labels_citas_pendientes.grid(row=1, column=0)

        self.label_empty_citas_pendientes = tk.Label(self.frame_title_citas_pendientes,
                                              text="                                                         ",
                                              background="black", font=("Candara", 30))
        self.label_empty_citas_pendientes2 = tk.Label(self.frame_title_citas_pendientes,
                                               text="                                                         ",
                                               background="black", font=("Candara", 30))

        texto_citas=ciclo_obtener_texto_citas()

        self.label_title_citas_pendientes = tk.Label(self.frame_title_citas_pendientes, text="doctor's office")
        self.label_title_citas_pendientes.config(font=("Candara", 48), fg="white", background="black",
                                    image=self.imagen_boton_obtener_citas_pendientes)

        self.label_citas_pendientes= tk.Label(self.frame_labels_citas_pendientes, text=str(texto_citas))
        self.label_citas_pendientes.config(font=("Arial rounded MT", 11), fg="white", background="black")

        self.boton_return_citas_pendientes = tk.Button(self.frame_labels_citas_pendientes, borderwidth=0,
                                                   image=self.imagen_boton_volver_menu_registrar,
                                                   background="black",
                                                   command=self.return_citas_pendientes_a_menu)
        self.boton_return_citas_pendientes.grid(row=3, column=1)


        self.label_citas_pendientes.grid(row=1,column=1)
        self.label_empty_citas_pendientes.grid(row=0, column=0)
        self.label_title_citas_pendientes.grid(row=0, column=1)
        self.label_empty_citas_pendientes2.grid(row=0, column=2)





    def return_registrar_a_menu(self):
        self.ventana_registrar.destroy()
        self.window.iconify()
        self.window.state("zoomed")

    def return_delete_a_menu(self):
        self.ventana_delete.destroy()
        self.window.iconify()
        self.window.state("zoomed")

    def return_registrar_medical_appointment_a_menu(self):
        self.ventana_registrar_cita.destroy()
        self.window.iconify()
        self.window.state("zoomed")

    def return_confirm_medical_appointment_a_menu(self):
        self.ventana_confirmar_cita.destroy()
        self.window.iconify()
        self.window.state("zoomed")

    def return_cancel_medical_appointment_a_menu(self):
        self.ventana_cancelar_cita.destroy()
        self.window.iconify()
        self.window.state("zoomed")

    def return_atender_medical_appointment_a_menu(self):
        self.ventana_atender_cita.destroy()
        self.window.iconify()
        self.window.state("zoomed")

    def return_citas_pendientes_a_menu(self):
        self.ventana_citas_pendientes.destroy()
        self.window.iconify()
        self.window.state("zoomed")

    def return_elegir_a_menu(self):
        self.ventana_atender_cita.destroy()
        self.ventana_elegir.destroy()
        self.window.iconify()
        self.window.state("zoomed")

    def return_historia_paciente_a_menu(self):
        self.ventana_historial_paciente.destroy()
        self.window.iconify()
        self.window.state("zoomed")


    def historial_paciente(self):
        self.window.withdraw()
        self.ventana_historial_paciente = tk.Toplevel()
        self.ventana_historial_paciente.maxsize(1280, 720)
        self.ventana_historial_paciente.state("zoomed")
        self.ventana_historial_paciente.iconbitmap("images/logo_ventana.ico")
        self.ventana_historial_paciente.geometry("1280x820")
        self.ventana_historial_paciente.title("Registrar cita")
        self.ventana_historial_paciente.resizable(True, True)
        self.ventana_historial_paciente.config(background="black")
        self.frame_historial_paciente = tk.Frame(self.ventana_historial_paciente)
        self.frame_historial_paciente.config(background="black")
        self.frame_historial_paciente.grid(row=0, column=1)
        self.frame_botones_historial_paciente = tk.Frame(self.ventana_historial_paciente)
        self.frame_botones_historial_paciente.config(background="black")
        self.frame_botones_historial_paciente.grid(row=1, column=1)

        self.frame_botones_padre_historial_cita = tk.Frame(self.ventana_historial_paciente)
        self.frame_botones_padre_historial_cita.config(background="black")
        self.frame_botones_padre_historial_cita.grid(row=2, column=1)

        self.label_titulo_historial_cita = tk.Label(self.frame_historial_paciente, text="Consultorio")
        self.label_titulo_historial_cita.config(font=("Candara", 48), fg="white", background="black",
                                                image=self.imagen_titulo_pequena)
        self.label_titulo_historial_cita.grid(row=0, column=1)

        self.label_vacio_historial_cita = tk.Label(self.frame_historial_paciente,
                                                   text="                                                         ",
                                                   background="black", font=("Candara", 30))
        self.label_vacio_historial_cita2 = tk.Label(self.frame_historial_paciente,
                                                    text="                                                         ",
                                                    background="black", font=("Candara", 30))
        self.label_vacio_historial_cita.grid(row=0, column=0)
        self.label_vacio_historial_cita2.grid(row=0, column=2)

        self.cedula_historial_cita= tk.Label(self.frame_botones_historial_paciente)
        self.cedula_historial_cita.config(font=("Candara", 48), fg="white", background="black",
                                          image=self.imagen_boton_registrar_cedula)
        self.cedula_historial_cita.grid(row=2, column=0)
        self.entrada_cedula_historial_cita = tk.Entry(self.frame_botones_historial_paciente, font=("Arial rounded MT", 18),
                                                      bd=4, width=30,
                                                      justify="center")
        self.entrada_cedula_historial_cita.grid(row=2, column=1)


        self.boton_get_info_historial_paciente = tk.Button(self.frame_botones_padre_historial_cita, borderwidth=0,
                                                       image=self.imagen_boton_historial_paciente, background="black",
                                                       command="")
        self.boton_get_info_historial_paciente.grid(row=0, column=1)

        self.boton_return_historial_cita = tk.Button(self.frame_botones_padre_historial_cita, borderwidth=0,
                                                     image=self.imagen_boton_volver_menu_registrar,
                                                     background="black",
                                                     command=self.return_historia_paciente_a_menu)
        self.boton_return_historial_cita.grid(row=0, column=0)





def ciclo_obtener_texto_citas():

    text: str = ""
    text_acumulado:str=""
    citas_pacientes_no_atendidos = {"0": ["1000204245", "Juan Esteban" ], "1": ["1000203456","Pepito"]}

    for cita in citas_pacientes_no_atendidos:
        text = (f"La identificacion de la cita es : {cita} -> El nombre del paciente es : {citas_pacientes_no_atendidos[cita][1]} -> "
                f"y la cedula del paciente es : {citas_pacientes_no_atendidos[cita][0]}\n")
        text_acumulado += text + "\n"

    return text_acumulado





















