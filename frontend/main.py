from UI import UI
from modelo import Consultorio
from controlador import Controlador

if __name__ == '__main__':
    controlador = Controlador(UI(), Consultorio())
    controlador.start()

