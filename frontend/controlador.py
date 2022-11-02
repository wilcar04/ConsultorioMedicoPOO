from UI import UI
from modelo import Consultorio
from exceptions import *


class Controlador:
    def __init__(self, vista: UI, modelo: Consultorio):
        self.vista: UI = vista
        self.modelo: Consultorio = modelo

    def start(self):
        self.vista.create_ventana_principal(self)


    def click_registrar_usuario(self):
        self.vista.registrar(self)

    def click_obtener_registrar_usuario(self):
        datos = self.vista.get_info_registrar()
        try:
            self.modelo.registrar_ususario(datos["id"],datos["name"],datos["gender"],datos["date"],datos["cel_get_info"])
        except UsuarioYaRegistradoError:
            pass
        self.vista.finalizar_registrar()



    def click_eliminar_paciente(self):

        pass

    def click_asignar_cita(self):
        pass

    def click_confirmar_cita(self):
        pass

    def click_cancelar_cita(self):
        pass

    def click_atender_cita(self):
        pass

    def click_obtener_agenda_dia(self):
        pass

    def click_obtener_historial_paciente(self):
        pass

    def click_obtener_citas(self):
        pass