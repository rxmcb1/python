import random

def simular_sensores():
    # Simula sensores con valores aleatorios: True (movimiento) o False (sin movimiento)
    sensores = [random.choice([True, False]) for _ in range(3)]
    return sensores

def detectar_intrusos():
    alarma_activada = True  # Inicialmente activa
    es_noche = input("¿Es de noche? (s/n): ").strip().lower() == 's'
    
    while True:
        print("\n--- Menú del Sistema de Seguridad ---")
        print("1. Simular sensores")
        print("2. Activar/Desactivar alarma")
        print("3. Volver al menú principal")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            sensores = simular_sensores()
            print(f"Estado de sensores: {sensores}")
            detecciones = sensores.count(True)
            if alarma_activada and es_noche and detecciones >= 2:
                print("🚨 ¡ALERTA! Movimiento detectado. Alarma activada.")
            else:
                print("✅ Todo en orden. La alarma no se activa.")

        elif opcion == '2':
            if alarma_activada:
                alarma_activada = False
                print("🔕 La alarma ha sido DESACTIVADA.")
            else:
                alarma_activada = True
                print("🔔 La alarma ha sido ACTIVADA.")

        elif opcion == '3':
            break

        elif opcion == '4':
            print("Saliendo del sistema...")
            exit()

        else:
            print("Opción no válida. Intenta de nuevo.")

def menu_principal():
    while True:
        print("\n===== Bienvenido al Sistema de Seguridad =====")
        print("Este programa simula la detección de intrusos con 3 sensores de movimiento.")
        print("La alarma se activa si al menos 2 sensores detectan movimiento y es de noche.")
        print("----------------------------------------------")
        print("1. Ejecutar ejercicio de detección de intrusos")
        print("2. Volver a hacer otro ejercicio")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            detectar_intrusos()
        elif opcion == '2':
            print("🔁 Reiniciando el ejercicio...")
            continue  # Vuelve a mostrar el menú
        elif opcion == '3':
            print("👋 Gracias por usar el sistema. Hasta luego.")
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")

# Ejecutar el menú principal
menu_principal()
