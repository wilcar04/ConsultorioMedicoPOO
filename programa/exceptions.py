class FechaIncorrectaError(Exception):
    pass


class UsuarioNoRegistradoError(Exception):
    pass


class UsuarioYaRegistradoError(Exception):
    pass


class CitaIncorrectaError(Exception):
    pass


class PacienteNoTieneCitaError(Exception):
    pass


class PacienteYaTieneCitaError(Exception):
    pass


class EcografiaIncorrectaError(Exception):
    pass


class PacienteSinHistorialError(Exception):
    pass


class HoraIndicadaYaOcupadaError(Exception):
    pass


class MesNoValidoError(Exception):
    pass


class DiaNoValidoError(Exception):
    pass


class HoraNoValidaError(Exception):
    pass


class FechaSinCitasError(Exception):
    pass


class FechaNacimientoNoValidaError(Exception):
    pass