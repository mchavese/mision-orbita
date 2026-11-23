
# ====================================================================
# Archivo: ejercicio6_viaje.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV0
# Fecha: Noviembre 2026
# Versión: 1.0
# Descripción: Simula día a día el viaje hacia el destino y el consumo
#              de recursos de la nave.
# ====================================================================

# --- Constantes (Consumo de recursos por día) ---
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_DIA = 1

# --- Entrada de datos ---
dias_viaje = int(input("Ingrese la cantidad de días del viaje: "))
cantidad_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))

combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# --- Inicialización de variables de control ---
dias_transcurridos = 0
puede_continuar = True

# --- Simulación del viaje ---
print("\n--- Simulación del Viaje ---")

while dias_transcurridos < dias_viaje and puede_continuar == True:

    # Verificar los recursos antes de realizar el consumo diario
    combustible_insuficiente = combustible < CONSUMO_COMBUSTIBLE_DIA
    oxigeno_insuficiente = oxigeno < (cantidad_tripulantes * CONSUMO_OXIGENO_DIA)
    energia_insuficiente = energia < CONSUMO_ENERGIA_DIA
    provisiones_insuficientes = provisiones < (cantidad_tripulantes * CONSUMO_PROVISIONES_DIA)

    # --- Decisión: Verificar si todos los recursos son suficientes ---
    if (combustible_insuficiente == False and
        oxigeno_insuficiente == False and
        energia_insuficiente == False and
        provisiones_insuficientes == False):

        # Descontar el consumo correspondiente al día
        combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
        oxigeno = oxigeno - (cantidad_tripulantes * CONSUMO_OXIGENO_DIA)
        energia = energia - CONSUMO_ENERGIA_DIA
        provisiones = provisiones - (cantidad_tripulantes * CONSUMO_PROVISIONES_DIA)

        # Actualizar el contador de días completados
        dias_transcurridos = dias_transcurridos + 1

        # Mostrar el estado actualizado de los recursos
        print("Día", dias_transcurridos,
              "| Combustible:", combustible,
              "| Oxígeno:", oxigeno,
              "| Energía:", energia,
              "| Provisiones:", provisiones)

    else:
        # --- Mostrar los recursos insuficientes ---
        print("Viaje interrumpido en el día", dias_transcurridos + 1, ".")

        if combustible_insuficiente == True:
            print("Combustible insuficiente.")

        if oxigeno_insuficiente == True:
            print("Oxígeno insuficiente.")

        if energia_insuficiente == True:
            print("Energía insuficiente.")

        if provisiones_insuficientes == True:
            print("Provisiones insuficientes.")

        print("Días completados:", dias_transcurridos)

        # Cambiar la variable de control para finalizar el ciclo
        puede_continuar = False

# --- Salida de resultados ---
if dias_transcurridos == dias_viaje:
    print("\nLa nave llegó al destino en", dias_transcurridos, "días.")

print("\n--- Recursos Restantes ---")
print("Combustible:", combustible, "unidades")
print("Oxígeno:", oxigeno, "unidades")
print("Energía:", energia, "unidades")
print("Provisiones:", provisiones, "unidades")
