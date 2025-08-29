import time
import random

def controlar_luces():
    luces_encendidas = False
    es_noche = input("¿Es de noche? (s/n): ").strip().lower() == 's'

    while True:
        print("\n--- Menú del Sistema de Control de Luces ---")
        print("1. Simular sistema")
        print("2. Cambiar condición de día/noche")
        print("3. Volver al menú principal")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            print("Iniciando simulación del sistema domótico de luces (presiona Ctrl+C para detener)...")
            try:
                while True:
                    # Simular detección de movimiento
                    hay_movimiento = random.choice([True, False])
                    print(f"\nMovimiento detectado: {hay_movimiento}")
                    print(f"Es de noche: {es_noche}")

                    # Evaluar condiciones
                    if es_noche and hay_movimiento:
                        luces_encendidas = True
                        print("💡 Luces ENCENDIDAS.")
                    else:
                        luces_encendidas = False
                        print("💡 Luces APAGADAS.")

                    print("Esperando 10 segundos para la próxima lectura...\n")
                    time.sleep(10)

            except KeyboardInterrupt:
                print("\n⏹️ Simulación detenida por el usuario.")

        elif opcion == '2':
            es_noche = input("¿Es de noche ahora? (s/n): ").strip().lower() == 's'
            print(f"Condición de noche actualizada a: {es_noche}")

        elif opcion == '3':
            break

        elif opcion == '4':
            print("👋 Saliendo del sistema...")
            exit()

        else:
            print("❌ Opción no válida. Intenta de nuevo.")

def menu_principal():
    while True:
        print("\n===== Menú Principal del Sistema Domótico =====")
        print("1. Control de luces automático")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            controlar_luces()
        elif opcion == '2':
            print("👋 Gracias por usar el sistema. Hasta pronto.")
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")

# Ejecutar el menú principal
menu_principal()
