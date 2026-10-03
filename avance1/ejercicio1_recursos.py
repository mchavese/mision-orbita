# ====================================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCVO
# Fecha: Octubre 2026
# Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión espacial.
# ====================================================================

# --- Constantes (Valores fijos de consumo y reserva) ---
CONSUMO_COMBUSTIBLE_POR_DIA = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_POR_DIA = 2
OXIGENO_EMERGENCIA = 5
CONSUMO_ENERGIA_POR_DIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_POR_DIA = 1
PROVISIONES_ADICIONALES = 3

# --- Entrada de datos ---
nombre_mision = input("Ingrese el nombre de la misión: ")
cantidad_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días estimados para llegar al destino: "))

# --- Procesamiento (Cálculos de recursos) ---
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_POR_DIA
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_POR_DIA
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

oxigeno_requerido = (dias_viaje * cantidad_tripulantes * CONSUMO_OXIGENO_POR_DIA) + OXIGENO_EMERGENCIA
energia_requerida = (dias_viaje * CONSUMO_ENERGIA_POR_DIA) + ENERGIA_EXPLORACION
provisiones_requeridas = (dias_viaje * cantidad_tripulantes * CONSUMO_PROVISIONES_POR_DIA) + PROVISIONES_ADICIONALES

# --- Salida de resultados ---
print("\n--- Resumen de Recursos Requeridos ---")
print("Misión:", nombre_mision)
print("Tripulantes:", cantidad_tripulantes)
print("Duración estimada hasta el destino:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")