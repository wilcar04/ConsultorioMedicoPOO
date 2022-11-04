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
            self.vista.excepcion("Usuario ya registrado")
        else:
            self.vista.finalizar_registrar()

    def click_eliminar_paciente(self):
        self.vista.delete(self)

    def click_obtener_eliminar_paciente(self):
        cedula = self.vista.delete_user()

        try:
            self.modelo.eliminar_paciente(cedula)
        except UsuarioNoRegistradoError:
            self.vista.excepcion("Usuario no registrado")
        else:
            self.vista.finalizar_eliminar()

    def click_asignar_cita(self):
        self.vista.registrar_medical_appointment(self)

    def click_obtener_asignar_cita(self):
        datos = self.vista.get_info_registrar_medical_appointment()
        try:
            self.modelo.asignar_cita(datos["cedula"], datos["mes"], datos["dia"], datos["hora"], datos["tipo_ecografia"])
        except UsuarioNoRegistradoError:
            self.vista.excepcion("La cédula ingresada no está registrada.")
        except PacienteYaTieneCitaError:
            self.vista.excepcion("El Paciente ya tiene una cita asignada.")
        except MesNoValidoError:
            self.vista.excepcion("Ingresaste un mes no válido.")
        except DiaNoValidoError:
            self.vista.excepcion("Ingresaste un dia no válido.")
        except HoraNoValidaError:
            self.vista.excepcion("Ingresaste una hora no válida.")
        except HoraIndicadaYaOcupadaError:
            self.vista.excepcion("La hora indicada ya se encuentra ocupada.")
        except EcografiaIncorrectaError:
            self.vista.excepcion("La Ecografía no está bien ingresada")
        else:
            self.vista.finalizar_registrar_cita()

    def click_confirmar_cita(self):
        self.vista.confirm_medical_appointment(self)

    def click_obtener_confirmar_cita(self):
        cedula = self.vista.get_info_confirmar_cita()
        try:
            self.modelo.confimar_cita(cedula)
        except UsuarioNoRegistradoError:
            self.vista.excepcion("Usuario no registrado")
        except PacienteNoTieneCitaError:
            self.vista.excepcion("El paciente no tiene cita")
        else:
            self.vista.finalizar_confirmar()

    def click_cancelar_cita(self):
        self.vista.delete_medical_appointment(self)

    def click_obtener_cancelar_cita(self):
        cedula = self.vista.get_info_cancelar_cita()
        try:
            self.modelo.cancelar_cita(cedula)
        except UsuarioNoRegistradoError:
            self.vista.excepcion("El Usuario no esta registrado")
        except PacienteNoTieneCitaError:
            self.vista.excepcion("El Usuario no tiene cita")

        else:
            self.vista.finalizar_cancelar_cita()

    def click_atender_cita(self):
        self.vista.atender_cita_medica(self)

    def click_obtener_atender_cita(self):

        cedula= self.vista.get_info_atender_cita()
        if not self.modelo.usuario_existe(cedula):
            self.vista.excepcion("El Usuario no esta registrado")
        else:
            self.crear_ventana_elegir_atender_cita()



    def crear_ventana_elegir_atender_cita(self):
        self.vista.ventana_elegir_atender_cita(self)

    def click_historia_clinica_atender_cita(self):
        historia=self.vista.proceso_historia_medica()
        try:
            self.modelo.atender_cita(historia[0],historia[1])
        except PacienteNoTieneCitaError:
            self.vista.excepcion("El paciente no tiene cita asignada")

        else:
            self.vista.finalizar_atender_cita()

    def click_examen_resultados_atender_cita(self):
        examen=self.vista.proceso_resultado_examen()
        try:
            self.modelo.atender_cita(examen[0],examen[1])
        except PacienteNoTieneCitaError:
            self.vista.excepcion("El paciente no tiene cita asignada")
        else:
            self.vista.finalizar_atender_cita()

    def click_obtener_agenda_cita(self):
        lista_mes_dia = self.vista.obtener_la_agenda_de_las_citas_pendientes()
        try:
            tupla_citas = self.modelo.obtener_agenda_dia(lista_mes_dia[0], int(lista_mes_dia[1]))
        except MesNoValidoError:
            self.vista.excepcion("El mes ingresado no es válido")
        except DiaNoValidoError:
            self.vista.excepcion("El día ingresado no es válido")
        except FechaSinCitasError:
            self.vista.excepcion("La fecha ingresada no tiene citas")
        else:
            txt = self.modelo.traducir_tupla(tupla_citas)
            self.vista.crear_ventana_mostrar_info_citas_pendientes(txt)



    def click_obtener_agenda_cita_dia(self):
        self.vista.obtener_la_agenda_de_las_citas_pendientes_dia(self)

    def click_obtener_historial_paciente_cedula(self):
        self.vista.historial_paciente(self)

    def click_obtener_ultima_historia_medica(self):
        try:
            cedula=self.vista.get_info_historial_paciente()
            historial_paciente=self.modelo.obtener_historial_paciente(cedula)
        except UsuarioNoRegistradoError:
            self.vista.excepcion("El usuario no esta registrado")
        except PacienteSinHistorialError:
            self.vista.excepcion("El paciente no tiene historia medica")
        else:
            self.vista.ventana_historial_paciente.destroy()
            print(f"La fecha de la historia clinica es {historial_paciente}")
