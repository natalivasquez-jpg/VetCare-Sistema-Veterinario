from datetime import datetime
from models import (
    Propietario, Mascota, Veterinario, ClinicaVeterinaria,
    ConsultaGeneral, Vacunacion, Desparasitacion,
    DatosInvalidosError, MascotaNoRegistradaError, CitaNoDisponibleError
)


def ejecutar_sistema():
    print("=" * 62)
    print("       VETCARE - SISTEMA DE GESTIÓN VETERINARIA")
    print("=" * 62)

    clinica = ClinicaVeterinaria("VetCare")

    # Creación de propietarios y mascotas (más de ocho objetos).
    propietario1 = Propietario("Laura Gómez", "3001234567")
    propietario2 = Propietario("Carlos Pérez", "3107654321")
    propietario3 = Propietario("Ana Ruiz", "3209876543")

    mascota1 = Mascota("Max", "Perro", 4, propietario1)
    mascota2 = Mascota("Luna", "Gato", 2, propietario2)
    mascota3 = Mascota("Rocky", "Perro", 6, propietario3)

    for mascota in (mascota1, mascota2, mascota3):
        clinica.registrar_mascota(mascota)

    veterinario1 = Veterinario("Dra. Camila Torres", "Medicina general")
    veterinario2 = Veterinario("Dr. Andrés López", "Medicina preventiva")

    # Colección heterogénea: contiene tres tipos distintos de servicios.
    servicios = [
        ConsultaGeneral(),
        Vacunacion(2),
        Desparasitacion(12.5)
    ]

    print("\n--- DEMOSTRACIÓN DE POLIMORFISMO ---")
    for servicio in servicios:
        print(f"{servicio.nombre}: ${servicio.calcular_costo():.2f}")
        print(f"Recomendación: {servicio.generar_recomendacion()}\n")

    print("--- PROGRAMACIÓN DE CITAS ---")
    cita1 = clinica.programar_cita(
        mascota1, veterinario1, servicios[0], datetime(2026, 11, 10, 9, 0)
    )
    cita2 = clinica.programar_cita(
        mascota2, veterinario2, servicios[1], datetime(2026, 11, 10, 10, 0)
    )
    cita3 = clinica.programar_cita(
        mascota3, veterinario1, servicios[2], datetime(2026, 11, 10, 11, 0)
    )

    for cita in (cita1, cita2, cita3):
        cita.confirmar()
        cita.completar()
        print(cita.resumen())

    print("\n--- HISTORIAL CLÍNICO DE MAX ---")
    for registro in mascota1.consultar_historial():
        print(registro)

    # Casos excepcionales: se capturan para que el programa continúe.
    print("\n--- PRUEBAS DE EXCEPCIONES ---")

    try:
        mascota_inexistente = Mascota("Toby", "Perro", 3, propietario1)
        clinica.programar_cita(
            mascota_inexistente, veterinario2, ConsultaGeneral(),
            datetime(2026, 11, 10, 12, 0)
        )
    except MascotaNoRegistradaError as error:
        print(f"Error controlado: {error}")

    try:
        clinica.programar_cita(
            mascota1, veterinario1, ConsultaGeneral(),
            datetime(2026, 11, 10, 9, 0)
        )
    except CitaNoDisponibleError as error:
        print(f"Error controlado: {error}")

    try:
        Vacunacion(0)
    except DatosInvalidosError as error:
        print(f"Error controlado: {error}")

    print("\nEl sistema continúa ejecutándose correctamente.")
    print("Fin de la demostración.")


if __name__ == "__main__":
    ejecutar_sistema()
