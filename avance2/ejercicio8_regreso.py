
# ====================================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV0
# Fecha: Noviembre 2026
# Versión: 1.0
# Descripción: Evalúa el regreso de la nave y calcula la supervivencia
#              de la tripulación cuando queda varada.
# ====================================================================

# --- Constantes (Consumo de recursos por día) ---
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_DIA = 1

# --- Entrada de datos ---
cantidad_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje_ida = int(input("Ingrese los días del viaje de ida: "))

combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# --- Inicialización de variables de control ---
dias_regreso = 0
puede_continuar = True

combustible_requerido_regreso = dias_viaje_ida * CONSUMO_COMBUSTIBLE_DIA

# --- Decisión: Verificar si existe combustible para regresar ---
print("\n--- Evaluación del Regreso ---")

if combustible >= combustible_requerido_regreso:

    print("La nave cuenta con combustible suficiente para regresar.")

    # --- Simulación del viaje de regreso ---
    while dias_regreso < dias_viaje_ida and puede_continuar == True:

        # Verificar los recursos antes del consumo diario
        combustible_insuficiente = combustible < CONSUMO_COMBUSTIBLE_DIA
        oxigeno_insuficiente = oxigeno < (cantidad_tripulantes * CONSUMO_OXIGENO_DIA)
        energia_insuficiente = energia < CONSUMO_ENERGIA_DIA
        provisiones_insuficientes = provisiones < (cantidad_tripulantes * CONSUMO_PROVISIONES_DIA)

        # --- Decisión: Comprobar disponibilidad de recursos ---
        if (combustible_insuficiente == False and
            oxigeno_insuficiente == False and
            energia_insuficiente == False and
            provisiones_insuficientes == False):

            # Descontar el consumo diario
            combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
            oxigeno = oxigeno - (cantidad_tripulantes * CONSUMO_OXIGENO_DIA)
            energia = energia - CONSUMO_ENERGIA_DIA
            provisiones = provisiones - (cantidad_tripulantes * CONSUMO_PROVISIONES_DIA)

            # Actualizar contador de días
            dias_regreso = dias_regreso + 1

            # Mostrar recursos restantes
            print("Día", dias_regreso,
                  "| Combustible:", combustible,
                  "| Oxígeno:", oxigeno,
                  "| Energía:", energia,
                  "| Provisiones:", provisiones)

        else:
            # --- Interrupción del regreso ---
            print("\nEl regreso se interrumpió en el día", dias_regreso + 1, ".")

            if combustible_insuficiente == True:
                print("Combustible insuficiente.")

            if oxigeno_insuficiente == True:
                print("Oxígeno insuficiente.")

            if energia_insuficiente == True:
                print("Energía insuficiente.")

            if provisiones_insuficientes == True:
                print("Provisiones insuficientes.")

            print("La tripulación no completó el regreso.")

            puede_continuar = False

    # --- Resultado del regreso ---
    if dias_regreso == dias_viaje_ida:
        print("\nLa tripulación regresó exitosamente a la Tierra.")

    # --- Mostrar recursos restantes ---
    print("\n--- Recursos Restantes ---")
    print("Combustible:", combustible, "unidades")
    print("Oxígeno:", oxigeno, "unidades")
    print("Energía:", energia, "unidades")
    print("Provisiones:", provisiones, "unidades")

else:

    # --- Caso B: La tripulación queda varada ---
    print("La tripulación quedó varada en el destino.")

    # Calcular los días completos de supervivencia por recurso
    dias_oxigeno = oxigeno // (cantidad_tripulantes * CONSUMO_OXIGENO_DIA)
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // (cantidad_tripulantes * CONSUMO_PROVISIONES_DIA)

    # --- Determinar el menor valor mediante condicionales ---
    if dias_oxigeno <= dias_energia and dias_oxigeno <= dias_provisiones:
        dias_supervivencia = dias_oxigeno

    elif dias_energia <= dias_oxigeno and dias_energia <= dias_provisiones:
        dias_supervivencia = dias_energia

    else:
        dias_supervivencia = dias_provisiones

    # --- Identificar todos los recursos limitantes ---
    print("\n--- Evaluación de Supervivencia ---")
    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)

    print("Supervivencia estimada:", dias_supervivencia, "días")

    print("Recurso(s) limitante(s):", end=" ")

    if dias_oxigeno == dias_supervivencia:
        print("oxígeno", end="")

        if dias_energia == dias_supervivencia or dias_provisiones == dias_supervivencia:
            print(",", end=" ")

    if dias_energia == dias_supervivencia:
        print("energía", end="")

        if dias_provisiones == dias_supervivencia:
            print(",", end=" ")

    if dias_provisiones == dias_supervivencia:
        print("provisiones", end="")

    print()
