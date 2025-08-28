import random
import time

def mostrar_menu():
    print("\n--- MENÚ DE CONTROL DE TEMPERATURA EN INVERNADERO ---")
    print("1. Mensaje de bienvenida")
    print("2. Iniciar simulación de temperatura")
    print("3. Reiniciar sistema")
    print("4. Salir")

def mensaje_bienvenida():
    print("\n¡Bienvenido al sistema de control de temperatura en el invernadero!")
    print("Este sistema lee la temperatura cada 5 segundos y toma decisiones:")
    print("- Si la temperatura es menor a 10°C, se activa el calefactor 🔥")
    print("- Si la temperatura está entre 10°C y 25°C, el sistema está inactivo 💤")
    print("- Si la temperatura es mayor a 25°C, se activa el ventilador 💨\n")

def iniciar_simulacion():
    print("\nIniciando simulación del sensor de temperatura...")
    print("Presione Ctrl + C para detener la simulación.\n")
    try:
        while True:
            temperatura = round(random.uniform(5.0, 35.0), 2)
            print(f"Temperatura actual: {temperatura}°C")
            
            if temperatura < 10:
                print("Acción: Activando calefactor 🔥")
            elif temperatura > 25:
                print("Acción: Activando ventilador 💨")
            else:
                print("Acción: Sistema inactivo 💤")

            print("-----------------------------")
            time.sleep(5)  # Espera 5 segundos antes de la próxima lectura
    except KeyboardInterrupt:
        print("\nSimulación detenida por el usuario.\n")

def control_temperatura():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            mensaje_bienvenida()
        elif opcion == "2":
            iniciar_simulacion()
        elif opcion == "3":
            print("\nReiniciando sistema...\n")
        elif opcion == "4":
            print("\nGracias por utilizar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el sistema
if __name__ == "__main__":
    control_temperatura()
