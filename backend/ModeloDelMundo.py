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



