# Ejercicio 5 - Selección del destino y autorización de la misión
# Proyecto Misión Órbita - Avance 2

# Constantes de las opciones del menú
OPCION_LUNA = 1
OPCION_MARTE = 2
OPCION_EUROPA = 3

# Constantes de duración
DIAS_LUNA = 3
DIAS_MARTE = 5
DIAS_EUROPA = 7

# Constantes de consumo y reserva
COMBUSTIBLE_POR_DIA = 8
RESERVA_COMBUSTIBLE = 10
OXIGENO_POR_TRIPULANTE = 2
RESERVA_OXIGENO = 5
ENERGIA_POR_DIA = 5
RESERVA_ENERGIA = 10
PROVISIONES_POR_TRIPULANTE = 1
RESERVA_PROVISIONES = 3

# Datos iniciales
nombre_mision = input("Nombre de la misión: ")
tripulantes = int(input("Cantidad de tripulantes: "))

print("\nDestinos disponibles:")
print("1. Luna")
print("2. Marte")
print("3. Europa")
opcion_destino = int(input("Seleccione el destino (1, 2 o 3): "))

# Selección del destino
destino = ""
dias_viaje = 0

match opcion_destino:
    case 1:
        destino = "Luna"
        dias_viaje = DIAS_LUNA
    case 2:
        destino = "Marte"
        dias_viaje = DIAS_MARTE
    case 3:
        destino = "Europa"
        dias_viaje = DIAS_EUROPA
    case _:
        print("Opción de destino no válida. La misión no puede planificarse.")

# La misión solo se planifica si el destino es válido
if opcion_destino == OPCION_LUNA or opcion_destino == OPCION_MARTE or opcion_destino == OPCION_EUROPA:
    combustible = int(input("Combustible disponible: "))
    oxigeno = int(input("Oxígeno disponible: "))
    energia = int(input("Energía disponible: "))
    provisiones = int(input("Provisiones disponibles: "))

    # Cálculo de recursos
    combustible_ida = dias_viaje * COMBUSTIBLE_POR_DIA
    combustible_regreso = dias_viaje * COMBUSTIBLE_POR_DIA
    combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
    oxigeno_requerido = dias_viaje * tripulantes * OXIGENO_POR_TRIPULANTE + RESERVA_OXIGENO
    energia_requerida = dias_viaje * ENERGIA_POR_DIA + RESERVA_ENERGIA
    provisiones_requeridas = dias_viaje * tripulantes * PROVISIONES_POR_TRIPULANTE + RESERVA_PROVISIONES

    # Resumen de la misión
    print("\n--- Resumen de la misión ---")
    print("Misión:", nombre_mision)
    print("Destino:", destino)
    print("Tripulantes:", tripulantes)
    print("Duración del viaje de ida:", dias_viaje, "días")
    print("Combustible para llegar:", combustible_ida, "unidades")
    print("Combustible para regresar:", combustible_regreso, "unidades")
    print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
    print("Combustible total requerido:", combustible_total, "unidades")
    print("Oxígeno requerido:", oxigeno_requerido, "unidades")
    print("Energía requerida:", energia_requerida, "unidades")
    print("Provisiones requeridas:", provisiones_requeridas, "unidades")

    # Validación de los cuatro recursos mediante condicionales anidadas
    if combustible >= combustible_total:
        if oxigeno >= oxigeno_requerido:
            if energia >= energia_requerida:
                if provisiones >= provisiones_requeridas:
                    print("Lanzamiento autorizado.")
                else:
                    print("Lanzamiento no autorizado. La misión debe ser revisada.")
            else:
                print("Lanzamiento no autorizado. La misión debe ser revisada.")
        else:
            print("Lanzamiento no autorizado. La misión debe ser revisada.")
    else:
        print("Lanzamiento no autorizado. La misión debe ser revisada.")
