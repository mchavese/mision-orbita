# ====================================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCVO
# Fecha: Octubre 2026
# Versión: 1.0
# Descripción: Autorización general de lanzamiento según los 4 recursos.
# ====================================================================

# --- Constantes ---
RESERVA_COMBUSTIBLE = 10

# --- Entrada de datos ---
combustible_disponible = int(input("Ingrese combustible disponible: "))
combustible_ida = int(input("Ingrese combustible requerido para llegar (ida): "))
combustible_regreso = int(input("Ingrese combustible requerido para regresar: "))

oxigeno_disponible = int(input("Ingrese oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese oxígeno requerido: "))

energia_disponible = int(input("Ingrese energía disponible: "))
energia_requerida = int(input("Ingrese energía requerida: "))

provisiones_disponibles = int(input("Ingrese provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese provisiones requeridas: "))

# --- Procesamiento ---
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# --- Decisión: Condicional doble sin anidación ---
print("\n--- Estado de la Misión ---")
if (combustible_disponible >= combustible_total_requerido and
    oxigeno_disponible >= oxigeno_requerido and
    energia_disponible >= energia_requerida and
    provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")