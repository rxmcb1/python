import time
import random

def controlar_aire_acondicionado():
    while True:
        print("\n--- Menú del Sistema de Aire Acondicionado ---")
        print("1. Simular sensores de temperatura y humedad")
        print("2. Volver al menú principal")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            print("Iniciando simulación del aire acondicionado (presiona Ctrl+C para detener)...")
            try:
                while True:
                    temperatura = round(random.uniform(25, 35), 1)  # Temperatura entre 25.0 y 35.0
                    humedad = random.randint(40, 80)  # Humedad entre 40% y 80%
                    
                    print(f"\n🌡️ Temperatura: {temperatura} °C")
                    print(f"💧 Humedad: {humedad} %")

                    if (temperatura > 28 and humedad > 60) or temperatura > 30:
                        print("❄️ Aire acondicionado ENCENDIDO.")
                    else:
                        print("💤 Aire acondicionado APAGADO.")

                    print("Esperando 10 segundos para la próxima lectura...\n")
                    time.sleep(10)

            except KeyboardInterrupt:
                print("\n⏹️ Simulación detenida por el usuario.")

        elif opcion == '2':
            break

        elif opcion == '3':
            print("👋 Saliendo del sistema...")
            exit()

        else:
            print("❌ Opción no válida. Intenta de nuevo.")

def menu_principal():
    while True:
        print("\n===== Menú Principal del Sistema de Automatización =====")
        print("1. Control de aire acondicionado")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            controlar_aire_acondicionado()
        elif opcion == '2':
            print("👋 Gracias por usar el sistema. Hasta luego.")
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")

# Ejecutar el menú principal
menu_principal()
