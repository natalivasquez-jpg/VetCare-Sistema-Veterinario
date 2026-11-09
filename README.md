# VetCare – Sistema de Gestión Veterinaria

Proyecto final de Programación Orientada a Objetos desarrollado en Python.

## 1. Problema y objetivo
VetCare permite registrar mascotas y propietarios, administrar veterinarios, programar citas y conservar el historial de atenciones. Su objetivo es organizar la información básica de una clínica veterinaria mediante un programa orientado a objetos.

## 2. Requisitos
- Python 3.9 o superior.
- No requiere instalar librerías externas.

## 3. Ejecución
1. Descargue o clone el repositorio.
2. Abra la carpeta del proyecto en Visual Studio Code, PyCharm o IDLE.
3. Ejecute en la terminal:

```bash
python3 main.py
```

## 4. Estructura
- `main.py`: programa principal y demostración de casos normales y excepcionales.
- `models.py`: entidades, herencia, composición, polimorfismo y excepciones.
- `diagrama_uml.puml`: diagrama UML en PlantUML.
- `Diseño python.docx`: justificación técnica del diseño.

## 5. Conceptos de POO demostrados
- Encapsulamiento mediante atributos privados y propiedades.
- Abstracción con `ServicioVeterinario`.
- Herencia con `ConsultaGeneral`, `Vacunacion` y `Desparasitacion`.
- Sobrescritura de `calcular_costo()` y `generar_recomendacion()`.
- Polimorfismo mediante una lista heterogénea de servicios recorrida con un único ciclo.
- Composición: `Mascota` crea y contiene su `HistorialClinico`.
- Relaciones: `Propietario` registra mascotas; `Cita` relaciona mascota, veterinario y servicio.
- Excepciones personalizadas: `DatosInvalidosError`, `MascotaNoRegistradaError` y `CitaNoDisponibleError`.

## 6. Pruebas
El programa crea más de ocho objetos y ejecuta:
- Registro de mascotas.
- Programación y finalización de citas.
- Consulta del historial clínico.
- Recorrido polimórfico de servicios.
- Tres casos excepcionales capturados, tras los cuales el sistema continúa.

## 7. Uso de IA
Se utilizó ChatGPT como apoyo para proponer el contexto, organizar las clases, revisar la aplicación de conceptos de POO y preparar una primera versión de la documentación. El equipo debe ejecutar, revisar, comprender y adaptar el código antes de entregarlo.
