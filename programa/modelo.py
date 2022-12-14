import datetime
from abc import ABC, abstractmethod
from typing import Optional, Type
from exceptions import *


class Historial(ABC):

    def __init__(self, texto: str):
        self.fecha: datetime.date = datetime.date.today()
        self.texto: str = texto

    @abstractmethod
    def __str__(self):
        pass


class HistoriaClinica(Historial):

    def __init__(self, texto):
        super().__init__(texto)

    def __str__(self):
        return f"Fecha: {self.fecha}\n" \
               f"Resultado: {self.texto}"


class ResultadoEcografia(Historial):

    def __init__(self, texto, tipo_ecografia: str):
        super().__init__(texto)
        self.tipo_ecografia: str = tipo_ecografia

    def __str__(self):
        return f"Fecha: {self.fecha}\n" \
               f"Tipo de Ecografía: {self.tipo_ecografia}\n" \
               f"Resultado: {self.texto}"


class Cita(ABC):

    def __init__(self, fecha: datetime.date, hora: datetime.time, cedula_paciente: str):
        self.fecha: datetime.date = fecha
        self.hora: datetime.time = hora
        self.cedula_paciente: str = cedula_paciente
        self.confirmada: bool = False
        self.atendida: bool = False

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def crear_historial(self, texto: str) -> Historial:
        pass

    def cita_confirmada(self):
        self.confirmada = True

    def cita_atendida(self):
        self.atendida = True

    def obtener_fecha_hora(self) -> tuple[datetime.date, datetime.time]:
        return self.fecha, self.hora


class CitaMedica(Cita):

    def __init__(self, fecha: datetime.date, hora: datetime.time, cedula_paciente: str):
        super().__init__(fecha, hora, cedula_paciente)

    def __str__(self):
        return f"Fecha: {self.fecha}, Hora: {self.hora}"

    def crear_historial(self, texto: str) -> Historial:
        return HistoriaClinica(texto)


class CitaEcografia(Cita):

    def __init__(self, fecha: datetime.date, hora: datetime.time, cedula_paciente: str, tipo_ecografia: str):
        super().__init__(fecha, hora, cedula_paciente)
        self.tipo_ecografia: str = tipo_ecografia

    def __str__(self):
        return f"Fecha: {self.fecha}, Hora: {self.hora}, Tipo de Ecografía: {self.tipo_ecografia}"

    def crear_historial(self, texto: str) -> Historial:
        return ResultadoEcografia(texto, self.tipo_ecografia)


class Paciente:

    def __init__(self, cedula: str, nombre: str, sexo: str, fecha_nacimiento: datetime.date, celular: str):
        self.cedula: str = cedula
        self.nombre: str = nombre
        self.sexo: str = sexo
        self.fecha_nacimiento: datetime.date = fecha_nacimiento
        self.edad: int = self.calcular_edad(fecha_nacimiento)
        self.celular: str = celular
        self.cita: Optional[Cita] = None
        self.historial: list[Historial] = []
        self.marcado: bool = False

    def __str__(self):
        return f"Nombre: {self.nombre} Cedula: {self.cedula} Celular: {self.celular}"

    @staticmethod
    def calcular_edad(fecha_nacimiento: datetime.date) -> int:
        fecha_actual = datetime.date.today()
        return int(fecha_actual.strftime("%Y")) - int(fecha_nacimiento.strftime("%Y"))

    def paciente_tiene_cita(self) -> bool:
        return self.cita is not None

    def agregar_cita(self, cita: Cita):
        self.cita = cita

    def cita_confirmada(self):
        self.cita.cita_confirmada()

    def obtener_fecha_hora_de_cita(self) -> tuple[datetime.date, datetime.time]:
        return self.cita.obtener_fecha_hora()

    def eliminar_cita(self):
        self.cita = None

    def crear_historial(self, texto: str) -> Historial:
        return self.cita.crear_historial(texto)

    def agregar_historial(self, historial: Historial):
        self.historial.append(historial)

    def cita_atendida(self):
        self.cita.cita_atendida()

    def tiene_historial(self) -> bool:
        return self.historial != []

    def informacion_historia(self) -> str:
        historial = self.historial[len(self.historial) - 1]
        return str(historial)

    def marcar(self):
        self.marcado = True


class AgendaDiaria:

    def __init__(self, fecha: datetime.date):
        self.fecha: datetime.date = fecha
        self.citas: dict[datetime.time, Cita] = {}

    @staticmethod
    def cedula_paciente_por_cita(lista_citas: list[Cita]) -> list[tuple]:
        lista_cedulas_con_citas = []
        for cita in lista_citas:
            cedula = cita.cedula_paciente
            lista_cedulas_con_citas.append((cedula, cita))
        return lista_cedulas_con_citas

    def hora_disponible(self, hora: datetime.time) -> bool:
        return hora not in self.citas

    def agregar_cita(self, fecha: datetime.date, hora: datetime.time,
                     cedula_paciente: str, tipo_ecografia: str):
        if tipo_ecografia != "":
            cita = CitaEcografia(fecha, hora, cedula_paciente, tipo_ecografia)
        else:
            cita = CitaMedica(fecha, hora, cedula_paciente)
        self.citas[hora] = cita
        return cita

    def eliminar_cita(self, hora: datetime.time):
        del self.citas[hora]

    def lista_citas(self) -> list[Cita]:
        return [v for v in self.citas.values()]

    def obtener_horas(self) -> list[datetime.time]:
        horas = []
        for cita in self.citas.values():
            horas.append(cita.hora)
        return horas


class Agenda:

    def __init__(self):
        self.agendas_diarias: dict[datetime.date, AgendaDiaria] = {}

    def hora_disponible(self, dia: datetime.date, hora: datetime.time) -> bool:
        if dia in self.agendas_diarias:
            return self.agendas_diarias[dia].hora_disponible(hora)
        else:
            return True

    def agregar_cita(self, fecha: datetime.date, hora: datetime.time,
                     cedula_paciente: str, tipo_ecografia: str) -> Cita:
        if fecha not in self.agendas_diarias:
            self.agendas_diarias[fecha] = AgendaDiaria(fecha)
        return self.agendas_diarias[fecha].agregar_cita(fecha, hora, cedula_paciente, tipo_ecografia)

    def eliminar_cita(self, fecha: datetime.date, hora: datetime.time):
        self.agendas_diarias[fecha].eliminar_cita(hora)

    def fecha_tiene_citas(self, fecha: datetime.date) -> bool:
        return fecha in self.agendas_diarias

    def lista_citas_en_fecha(self, fecha: datetime.date) -> list[Cita]:
        return self.agendas_diarias[fecha].lista_citas()

    def cedula_paciente_por_cita(self, fecha: datetime.date, lista_citas: list[Cita]) -> list[tuple]:
        return self.agendas_diarias[fecha].cedula_paciente_por_cita(lista_citas)

    def obtener_horas(self, fecha: datetime.date) -> list[datetime.time]:
        return self.agendas_diarias[fecha].obtener_horas()


class Consultorio:
    HORA_INICIAL: int = 9
    HORA_FINAL: int = 16
    ECOGRAFIAS: tuple[str] = ("fetal", "abdominal", "vias urinarias", "mamaria", "muscular",
                              "cervical", "renal")

    def __init__(self):
        self.pacientes: dict[str, Paciente] = {}
        self.agenda: Agenda = Agenda()

    @staticmethod
    def obtener_numero_mes(mes: str) -> Optional[int]:
        meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
                 "agosto", "septiembre", "octubre", "noviembre", "diciembre")
        if mes.lower() in meses:
            return meses.index(mes.lower()) + 1
        else:
            return None

    @staticmethod
    def obtener_formato_fecha(numero_mes: int, dia: int) -> datetime.date:
        date = datetime.date.today()
        year = int(date.strftime("%Y"))
        return datetime.date(year, numero_mes, dia)

    @staticmethod
    def obtener_formato_hora(hora: int) -> datetime.time:
        return datetime.time(hora, 0)

    @staticmethod
    def dia_valido(dia: int, numero_mes: int) -> bool:
        if numero_mes in [1, 3, 5, 7, 8, 10, 12]:
            dias_del_mes = 31
        elif numero_mes in [4, 6, 9, 11]:
            dias_del_mes = 30
        else:
            dias_del_mes = 28
        return 0 < dia <= dias_del_mes

    def hora_valida(self, hora: int) -> bool:
        return self.HORA_INICIAL <= hora <= self.HORA_FINAL

    def usuario_existe(self, cedula: str) -> bool:
        return cedula in self.pacientes

    def buscar_paciente(self, cedula: str) -> Paciente:
        return self.pacientes[cedula]

    def informacion_paciente_por_cita(self, lista_cedulas_con_citas: list[Type[tuple]]) -> list[tuple[str, str]]:
        informacion = []
        for dato in lista_cedulas_con_citas:
            cedula, cita = dato
            paciente = self.buscar_paciente(cedula)
            informacion.append((str(paciente), str(cita)))
        return informacion

    def organizar_agenda(self, lista_horas: list[datetime.time],
                         lista_informacion: list[Type[tuple]]) -> tuple[Optional[Type[tuple]]]:
        agenda_organizada = []
        for hora in range(self.HORA_INICIAL, self.HORA_FINAL + 1):
            for hora_cita in lista_horas:
                if hora_cita.hour == hora:
                    index_hora_coincidente = lista_horas.index(hora_cita)
                    agenda_organizada.append(lista_informacion.pop(index_hora_coincidente))
                    lista_horas.pop(index_hora_coincidente)
                    break
            else:
                agenda_organizada.append(None)
        return tuple(agenda_organizada)

    def traducir_tupla(self, tupla_citas) -> str:
        texto = ""
        for i in range(len(tupla_citas)):
            texto += f"{self.HORA_INICIAL + i}: "
            if tupla_citas[i] is None:
                texto += "Cita disponible\n"
            else:
                texto += f"{tupla_citas[i][0]}\n"
        return texto[:-1]

    # Requisitos de programa:

    def registrar_ususario(self, cedula: str, nombre: str, sexo: str, fecha_nacimiento: str, celular: str):
        if not self.usuario_existe(cedula):
            formato_fecha = None
            try:
                lista_fecha = fecha_nacimiento.split("/")
                formato_fecha = datetime.date(int(lista_fecha[2]), int(lista_fecha[1]), int(lista_fecha[0]))
            except ValueError:
                raise FechaNacimientoNoValidaError
            paciente = Paciente(cedula, nombre, sexo, formato_fecha, celular)
            self.pacientes[cedula] = paciente
        else:
            raise UsuarioYaRegistradoError

    def eliminar_paciente(self, cedula: str):
        if not self.usuario_existe(cedula):
            raise UsuarioNoRegistradoError
        paciente = self.buscar_paciente(cedula)
        if paciente.paciente_tiene_cita():
            self.cancelar_cita(cedula)
        del self.pacientes[cedula]

    def asignar_cita(self, cedula: str, mes: str, dia: str, hora: str, tipo_ecografia: str):
        dia = int(dia)
        hora = int(hora)
        if not self.usuario_existe(cedula):
            raise UsuarioNoRegistradoError
        paciente = self.buscar_paciente(cedula)
        if paciente.paciente_tiene_cita():
            raise PacienteYaTieneCitaError
        numero_mes = self.obtener_numero_mes(mes)
        if numero_mes is None:
            raise MesNoValidoError
        if not self.dia_valido(dia, numero_mes):
            raise DiaNoValidoError
        formato_fecha = self.obtener_formato_fecha(numero_mes, dia)
        if not self.hora_valida(hora):
            raise HoraNoValidaError
        formato_hora = self.obtener_formato_hora(hora)
        if not self.agenda.hora_disponible(formato_fecha, formato_hora):
            raise HoraIndicadaYaOcupadaError
        if tipo_ecografia not in self.ECOGRAFIAS and tipo_ecografia != "":
            raise EcografiaIncorrectaError
        cita = self.agenda.agregar_cita(formato_fecha, formato_hora, cedula, tipo_ecografia)
        paciente.agregar_cita(cita)

    def confimar_cita(self, cedula: str):
        if self.usuario_existe(cedula):
            paciente = self.pacientes[cedula]
            if paciente.paciente_tiene_cita():
                paciente.cita_confirmada()
            else:
                raise PacienteNoTieneCitaError
        else:
            raise UsuarioNoRegistradoError

    def cancelar_cita(self, cedula: str):
        if self.usuario_existe(cedula):
            paciente = self.pacientes[cedula]
            if paciente.paciente_tiene_cita():
                (fecha, hora) = paciente.obtener_fecha_hora_de_cita()
                self.agenda.eliminar_cita(fecha, hora)
                paciente.eliminar_cita()
            else:
                raise PacienteNoTieneCitaError
        else:
            raise UsuarioNoRegistradoError

    def atender_cita(self, cedula: str, texto: str):
        if self.usuario_existe(cedula):
            paciente = self.pacientes[cedula]
            if paciente.paciente_tiene_cita():
                historial = paciente.crear_historial(texto)
                paciente.agregar_historial(historial)
                paciente.cita_atendida()
            else:
                raise PacienteNoTieneCitaError
        else:
            raise UsuarioNoRegistradoError

    def obtener_agenda_dia(self, mes: str, dia: int) -> tuple[Optional[Type[tuple]]]:
        numero_mes = self.obtener_numero_mes(mes)
        if numero_mes is None:
            raise MesNoValidoError
        if not self.dia_valido(dia, numero_mes):
            raise DiaNoValidoError
        fecha = self.obtener_formato_fecha(numero_mes, dia)
        if not self.agenda.fecha_tiene_citas(fecha):
            raise FechaSinCitasError
        lista_citas = self.agenda.lista_citas_en_fecha(fecha)
        lista_cedulas_con_citas = self.agenda.cedula_paciente_por_cita(fecha, lista_citas)
        lista_informacion = self.informacion_paciente_por_cita(lista_cedulas_con_citas)
        lista_horas = self.agenda.obtener_horas(fecha)
        return self.organizar_agenda(lista_horas, lista_informacion)

    def obtener_historial_paciente(self, cedula: str) -> str:
        if not self.usuario_existe(cedula):
            raise UsuarioNoRegistradoError
        paciente = self.buscar_paciente(cedula)
        if paciente.tiene_historial():
            return paciente.informacion_historia()
        else:
            raise PacienteSinHistorialError

    def marcar_paciente(self, cedula: str):
        if self.usuario_existe(cedula):
            paciente = self.buscar_paciente(cedula)
            paciente.marcar()
        else:
            raise UsuarioNoRegistradoError
