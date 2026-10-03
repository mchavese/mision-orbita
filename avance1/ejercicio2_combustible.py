# ====================================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCVO
# Fecha: Octubre 2026
# Versión: 1.0
# Descripción: Verifica el combustible y advierte si el margen es bajo.
# ====================================================================

# --- Constantes (Valores que no cambian) ---
RESERVA_EMERGENCIA = 10
MARGEN_MINIMO_ADVERTENCIA = 10

# --- Entrada de datos ---
combustible_disponible = int(input("Ingrese la cantidad de combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para llegar (ida): "))
combustible_regreso = int(input("Ingrese el combustible requerido para regresar: "))

# --- Procesamiento (Cálculos matemáticos) ---
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_EMERGENCIA
combustible_adicional = combustible_disponible - combustible_total_requerido

# --- Salida obligatoria permanente (Se muestra SIEMPRE) ---
print("\n--- Verificación de Combustible ---")
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_EMERGENCIA, "unidades")
print("Combustible total requerido:", combustible_total_requerido, "unidades")
print("Combustible adicional disponible:", combustible_adicional, "unidades")

# --- Condicional simple (Solo actúa si el margen es menor a 10) ---
if combustible_adicional < MARGEN_MINIMO_ADVERTENCIA:
    print("Advertencia: el margen adicional de combustible es bajo.")