class Paciente:
    lista_pacientes=[]
    def __init__(self,nombre:str,cedula:str,sexo:str,fecha_nacimiento:str,celular:str):
        self.nombre=nombre
        self.cedula:str=cedula
        self.sexo=sexo
        self.fecha_nacimiento=fecha_nacimiento
        self.celular=celular
        self.tiene_cita=False
        Paciente.lista_pacientes.append(self)

    def __repr__(self):
        return self.cedula

class Informacion:
    def __init__(self):
        self.informacion_registrar:list[dict]=[]
        self.informacion_eliminar:list[str]=[]
        self.informacion_registrar_cita:list[dict]=[]

    def agregrar_informacion_registrar(self,diccionario:dict):
        self.informacion_registrar.append(diccionario)
    def agregar_informacion_eliminar(self,cedula):
        self.informacion_eliminar.append(cedula)
    def agregar_informacion_registrar_cita(self,diccionario):
        self.informacion_registrar_cita.append(diccionario)




