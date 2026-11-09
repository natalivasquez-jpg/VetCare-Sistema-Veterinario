from abc import ABC, abstractmethod
from datetime import datetime

# Excepciones personalizadas 

class DatosInvalidosError(Exception):
    """Se utiliza cuando un dato obligatorio no cumple las reglas del sistema."""


class MascotaNoRegistradaError(Exception):
    """Se utiliza cuando se intenta atender una mascota que no está registrada."""


class CitaNoDisponibleError(Exception):
    """Se utiliza cuando el veterinario ya tiene una cita en el mismo horario."""


#  Entidades principales 

class HistorialClinico:
    """Almacena los registros de atención de una mascota."""

    def __init__(self):
        self.__registros = []

    def agregar_registro(self, descripcion):
        if not descripcion or not descripcion.strip():
            raise DatosInvalidosError("La descripción del registro no puede estar vacía.")
        self.__registros.append(descripcion.strip())

    def consultar_registros(self):
        return list(self.__registros)


class Propietario:
    def __init__(self, nombre, telefono):
        if not nombre.strip() or not telefono.strip():
            raise DatosInvalidosError("El propietario debe tener nombre y teléfono.")
        self.__nombre = nombre
        self.__telefono = telefono
        self.__mascotas = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def telefono(self):
        return self.__telefono

    def registrar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def listar_mascotas(self):
        return list(self.__mascotas)


class Mascota:
    def __init__(self, nombre, especie, edad, propietario):
        if not nombre.strip() or not especie.strip() or edad < 0:
            raise DatosInvalidosError("Datos de mascota no válidos.")
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__propietario = propietario
       
        self.__historial = HistorialClinico()
        propietario.registrar_mascota(self)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def especie(self):
        return self.__especie

    @property
    def propietario(self):
        return self.__propietario

    def agregar_atencion(self, descripcion):
        self.__historial.agregar_registro(descripcion)

    def consultar_historial(self):
        return self.__historial.consultar_registros()


class Veterinario:
    def __init__(self, nombre, especialidad):
        if not nombre.strip() or not especialidad.strip():
            raise DatosInvalidosError("El veterinario debe tener nombre y especialidad.")
        self.__nombre = nombre
        self.__especialidad = especialidad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def especialidad(self):
        return self.__especialidad


# Abstracción, herencia y polimorfismo

class ServicioVeterinario(ABC):
    """Clase abstracta: define la estructura común de los servicios."""

    def __init__(self, nombre, duracion_minutos):
        if duracion_minutos <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero.")
        self._nombre = nombre
        self._duracion_minutos = duracion_minutos

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def generar_recomendacion(self):
        pass


class ConsultaGeneral(ServicioVeterinario):
    def __init__(self):
        super().__init__("Consulta general", 30)
        self.__tarifa_base = 350.00

    def calcular_costo(self):
        return self.__tarifa_base

    def generar_recomendacion(self):
        return "Llevar a la mascota a revisión periódica y mantener su esquema preventivo."


class Vacunacion(ServicioVeterinario):
    def __init__(self, cantidad_dosis=1):
        super().__init__("Vacunación", 20)
        if cantidad_dosis <= 0:
            raise DatosInvalidosError("La cantidad de dosis debe ser mayor que cero.")
        self.__cantidad_dosis = cantidad_dosis
        self.__costo_por_dosis = 220.00

    def calcular_costo(self):
        return self.__cantidad_dosis * self.__costo_por_dosis

    def generar_recomendacion(self):
        return f"Registrar {self.__cantidad_dosis} dosis y respetar las fechas del esquema de vacunación."


class Desparasitacion(ServicioVeterinario):
    def __init__(self, peso_kg):
        super().__init__("Desparasitación", 15)
        if peso_kg <= 0:
            raise DatosInvalidosError("El peso debe ser mayor que cero.")
        self.__peso_kg = peso_kg
        self.__costo_por_kg = 18.00

    def calcular_costo(self):
        return self.__peso_kg * self.__costo_por_kg

    def generar_recomendacion(self):
        return f"Verificar el peso ({self.__peso_kg} kg) y programar la siguiente desparasitación."


class Cita:
    def __init__(self, mascota, veterinario, servicio, fecha_hora):
        self.__mascota = mascota
        self.__veterinario = veterinario
        self.__servicio = servicio
        self.__fecha_hora = fecha_hora
        self.__estado = "Programada"

    @property
    def veterinario(self):
        return self.__veterinario

    @property
    def fecha_hora(self):
        return self.__fecha_hora

    def confirmar(self):
        self.__estado = "Confirmada"

    def completar(self):
        self.__estado = "Completada"
        detalle = (
            f"{self.__fecha_hora:%d/%m/%Y %H:%M} - {self.__servicio.nombre} "
            f"con {self.__veterinario.nombre}. Costo: ${self.__servicio.calcular_costo():.2f}"
        )
        self.__mascota.agregar_atencion(detalle)

    def resumen(self):
        return (f"{self.__fecha_hora:%d/%m/%Y %H:%M} | {self.__mascota.nombre} | "
                f"{self.__servicio.nombre} | {self.__veterinario.nombre} | "
                f"${self.__servicio.calcular_costo():.2f} | {self.__estado}")


class ClinicaVeterinaria:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mascotas = []
        self.__citas = []

    def registrar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def programar_cita(self, mascota, veterinario, servicio, fecha_hora):
        if mascota not in self.__mascotas:
            raise MascotaNoRegistradaError(
                f"La mascota {mascota.nombre} no está registrada en la clínica."
            )
        for cita in self.__citas:
            if cita.veterinario == veterinario and cita.fecha_hora == fecha_hora:
                raise CitaNoDisponibleError(
                    f"{veterinario.nombre} ya tiene una cita a esa hora."
                )
        cita = Cita(mascota, veterinario, servicio, fecha_hora)
        self.__citas.append(cita)
        return cita

    def listar_citas(self):
        return [cita.resumen() for cita in self.__citas]
