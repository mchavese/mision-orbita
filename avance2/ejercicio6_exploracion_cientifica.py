# ====================================================================
# Archivo: ejercicio6_exploracion_cientifica.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV0
# Fecha: Noviembre 2026
# Versión: 1.0
# Descripción: Menú interactivo de actividades de exploración científica
#              con match-case, ciclo while y control de resultados.
# ====================================================================

# --- Constantes ---
OPCION_SALIR = 4

COSTO_MUESTRAS = 3
COSTO_ATMOSFERA = 2
COSTO_FOTOGRAFIAS = 1

PUNTOS_MUESTRAS = 10
PUNTOS_ATMOSFERA = 8
PUNTOS_FOTOGRAFIAS = 5

# --- Entrada de datos iniciales ---
nombre_mision = input("Ingrese el nombre de la misión: ")
energia_disponible = int(input("Ingrese la energía disponible para exploración: "))

# --- Variables de control y acumuladores ---
opcion = 0
cantidad_muestras = 0
cantidad_analisis = 0
cantidad_fotografias = 0
total_actividades = 0
energia_consumida = 0
puntos_cientificos = 0

# --- Ciclo del menú de actividades científicas ---
while opcion != OPCION_SALIR:
    print("\n=== Menú de Actividades Científicas ===")
    print("Energía disponible actual:", energia_disponible, "unidades")
    print("1. Recolección de muestras de suelo (Costo: 3 energía | +10 puntos)")
    print("2. Análisis atmosférico y radiación (Costo: 2 energía | +8 puntos)")
    print("3. Captura de fotografías y mapeo (Costo: 1 energía | +5 puntos)")
    print("4. Finalizar exploración y mostrar resumen")

    opcion = int(input("Seleccione una opción (1-4): "))

    match opcion:
        case 1:
            if energia_disponible >= COSTO_MUESTRAS:
                energia_disponible = energia_disponible - COSTO_MUESTRAS
                energia_consumida = energia_consumida + COSTO_MUESTRAS
                cantidad_muestras = cantidad_muestras + 1
                total_actividades = total_actividades + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_MUESTRAS
                print("Resultado: Muestras de suelo recolectadas con éxito (+10 puntos científicos).")
            else:
                print("Energía insuficiente para realizar la recolección de muestras.")

        case 2:
            if energia_disponible >= COSTO_ATMOSFERA:
                energia_disponible = energia_disponible - COSTO_ATMOSFERA
                energia_consumida = energia_consumida + COSTO_ATMOSFERA
                cantidad_analisis = cantidad_analisis + 1
                total_actividades = total_actividades + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_ATMOSFERA
                print("Resultado: Análisis atmosférico completado con éxito (+8 puntos científicos).")
            else:
                print("Energía insuficiente para realizar el análisis atmosférico.")

        case 3:
            if energia_disponible >= COSTO_FOTOGRAFIAS:
                energia_disponible = energia_disponible - COSTO_FOTOGRAFIAS
                energia_consumida = energia_consumida + COSTO_FOTOGRAFIAS
                cantidad_fotografias = cantidad_fotografias + 1
                total_actividades = total_actividades + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_FOTOGRAFIAS
                print("Resultado: Fotografías y mapeo registrados con éxito (+5 puntos científicos).")
            else:
                print("Energía insuficiente para capturar fotografías y mapeo.")

        case 4:
            print("Finalizando actividades de exploración científica...")

        case _:
            print("Opción no válida. Seleccione una opción del 1 al 4.")

# --- Salida de resultados finales ---
print("\n--- Resumen de Exploración Científica ---")
print("Misión:", nombre_mision)
print("Recolecciones de muestras realizadas:", cantidad_muestras)
print("Análisis atmosféricos realizados:", cantidad_analisis)
print("Capturas de fotografías y mapeo realizadas:", cantidad_fotografias)
print("Total de actividades completadas:", total_actividades)
print("Energía total consumida:", energia_consumida, "unidades")
print("Energía restante:", energia_disponible, "unidades")
print("Puntaje científico obtenido:", puntos_cientificos, "puntos")

if total_actividades > 0:
    print("Estado de la exploración: Actividades científicas completadas.")
else:
    print("Estado de la exploración: No se realizaron actividades científicas.")

