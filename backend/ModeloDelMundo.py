class Informacion:
    def __init__(self):
        self.informacion_registrar: list[dict] = []
        self.informacion_eliminar: list[str] = []
        self.informacion_registrar_cita: list[dict] = []
        self.informacion_confirmar_cita: list[str] = []
        self.informacion_eliminar_cita: list[str] = []
        self.informacion_historias_medicas: list[dict]=[]
        self.informacion_resultados_examenes:list[dict]=[]

    def agregar_informacion_registrar(self, diccionario: dict):
        self.informacion_registrar.append(diccionario)

    def agregar_informacion_eliminar(self, cedula):
        self.informacion_eliminar.append(cedula)

    def agregar_informacion_registrar_cita(self, diccionario):
        self.informacion_registrar_cita.append(diccionario)

    def agregar_informacion_confirmar_cita(self, cedula):
        self.informacion_confirmar_cita.append(cedula)

    def agregar_informacion_cancelar_cita(self,cedula):
        self.informacion_eliminar_cita.append(cedula)

    def agregar_informacion_historia_medica(self,diccionario):
        self.informacion_historias_medicas.append(diccionario)

    def agregar_informacion_resultados_examenes(self,diccionario):
        self.informacion_resultados_examenes.append(diccionario)
