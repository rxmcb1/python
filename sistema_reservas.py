def mostrar_menu():
    print("\n--- MENÚ DEL SISTEMA DE RESERVAS ---")
    print("1. Mensaje de bienvenida")
    print("2. Realizar una reserva")
    print("3. Reiniciar reservas")
    print("4. Salir")

def mensaje_bienvenida():
    print("\n¡Bienvenido al sistema de reservas de asientos!")
    print("Este programa permite reservar asientos en una sala de cine.")
    print("Puede hacer reservas hasta completar la capacidad total de la sala.")
    print("Capacidad total de la sala: 10 asientos.\n")

def realizar_reservas(asientos_disponibles):
    while asientos_disponibles > 0:
        print(f"\nAsientos disponibles: {asientos_disponibles}")
        nombre = input("Ingrese su nombre para reservar un asiento (o escriba 'salir' para cancelar): ").strip()
        if nombre.lower() == "salir":
            break
        if nombre == "":
            print("Nombre inválido. Intente de nuevo.")
            continue
        print(f"Reserva confirmada para {nombre}. ¡Gracias!")
        asientos_disponibles -= 1

    if asientos_disponibles == 0:
        print("\nTodos los asientos han sido reservados. Gracias por usar el sistema.")
    
    return asientos_disponibles

def sistema_reservas():
    asientos_disponibles = 10
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            mensaje_bienvenida()
        elif opcion == "2":
            if asientos_disponibles > 0:
                asientos_disponibles = realizar_reservas(asientos_disponibles)
            else:
                print("No hay asientos disponibles.")
        elif opcion == "3":
            print("\nReiniciando reservas...")
            asientos_disponibles = 10
        elif opcion == "4":
            print("\nGracias por utilizar el sistema de reservas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el sistema
if __name__ == "__main__":
    sistema_reservas()
