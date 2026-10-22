# Manifiesto de configuración

- **Proyecto:** lab-config-Yucra (reservas de equipos del laboratorio)
- **Versión:** v1.0.0
- **Cambio incluido:** CR-02 (máximo de 2 horas por reserva)
- **Línea base anterior:** v0.1.0 (máximo de 4 horas)
- **Fecha:** 22/10/2026

## Elementos de configuración controlados

| ID | Archivo | Responsable simulado |
|---|---|---|
| EC-01 | docs/requisitos.md | Analista |
| EC-02 | src/reservas.py | Desarrollador |
| EC-03 | tests/test_reservas.py | Probador |
| EC-04 | docs/cambios.md | Gestor |
| EC-05 | README.md | Gestor |

## Herramientas utilizadas

- Git: git version 2.54.0.windows.1
- Python: Python 3.14.5
- Sistema operativo: Windows 11

## Verificación

- **Comando de prueba:** `python -m unittest discover -s tests -v`
- **Resultado observado:** Ran 1 test (8 subcasos), OK
- **Casos cubiertos:** -1, 0, 1, 2, 3, 1.5, True y 2.0
- **Marcadores de conflicto:** ninguno

## Aprobación (simulada)

Revisado y aprobado por: Mariana Yucra, el 22/10/2026.
Nota: los roles de solicitante, desarrollador y revisor fueron simulados por una sola persona; no hubo revisión independiente.