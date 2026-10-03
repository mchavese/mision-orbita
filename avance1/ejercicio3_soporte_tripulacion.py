# ====================================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCVO
# Fecha: Octubre 2026
# Versión: 1.0
# Descripción: Determina si hay soporte vital suficiente para la tripulación.
# ====================================================================

# --- Entrada de datos ---
oxigeno_disponible = int(input("Ingrese la cantidad de oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese la cantidad de oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese la cantidad de provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese la cantidad de provisiones requeridas: "))

# --- Procesamiento y Decisión (Condicional doble con operador lógico 'and') ---
print("\n--- Resultado de Soporte ---")
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")