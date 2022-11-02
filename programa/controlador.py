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
            self.modelo.registrar_ususario(datos["id"], datos["name"], datos["gender"], datos["date"], datos["cel_get_info"])
        except UsuarioYaRegistradoError:
            self.vista.excepcion()
        else:
         self.vista.finalizar_registrar()

    def click_eliminar_paciente(self):
        self.vista.delete(self)

    def click_obtener_eliminar_paciente(self):
        cedula = self.vista.delete_user()

        try:
            self.modelo.eliminar_paciente(cedula)
        except UsuarioNoRegistradoError:
            self.vista.excepcion()
        else:
            self.vista.finalizar_eliminar()

    def click_asignar_cita(self):
        self.vista.registrar_medical_appointment(self)

    def click_obtener_asignar_cita(self):
        datos = self.vista.get_info_registrar_medical_appointment()
        try:
            self.modelo.asignar_cita(datos["cedula"], datos["mes"], datos["dia"], datos["hora"])
        except UsuarioNoRegistradoError:
            self.vista.excepcion()
        except PacienteYaTieneCitaError:
            self.vista.excepcion()
        except MesNoValidoError:
            self.vista.excepcion()
        except DiaNoValidoError:
            self.vista.excepcion()
        except HoraNoValidaError:
            self.vista.excepcion()
        except HoraIndicadaYaOcupadaError:
            self.vista.excepcion()
        except EcografiaIncorrectaError:
            self.vista.excepcion()
        else:
            self.vista.finalizar_asignar()

    def click_confirmar_cita(self):
        self.vista.confirm_medical_appointment(self)

    def click_obtener_confirmar_cita(self):
        cedula = self.vista.get_info_confirmar_cita()
        try:
            self.modelo.confimar_cita(cedula)
        except UsuarioNoRegistradoError:
            self.vista.excepcion()
        except PacienteNoTieneCitaError:
            self.vista.excepcion()
        else:
            self.vista.finalizar_confirmar()

    def click_cancelar_cita(self):
        self.vista.delete_medical_appointment(self)

    def click_obtener_cancelar_cita(self):
        cedula = self.vista.get_info_registrar_medical_appointment()
        try:
            self.modelo.cancelar_cita(cedula)
        except UsuarioNoRegistradoError:
            self.vista.excepcion()
        except PacienteNoTieneCitaError:
            self.vista.excepcion()

        else:
            self.vista.finalizar_cancelar_cita()

    def click_atender_cita(self):
        self.vista.atender_cita_medica(self)

    def click_obtener_atender_cita(self):
        datos = self.vista.proceso_historia_medica()
        try:
            self.modelo.atender_cita(datos["cedula"], datos["texto"])
        except UsuarioNoRegistradoError:
            self.vista.excepcion()
        except PacienteNoTieneCitaError:
            self.vista.excepcion()
        else:
            self.vista.finalizar_atender_cita()
