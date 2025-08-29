def controlar_acceso_tienda():
    while True:
        print("\n--- Menú del Sistema de Control de Acceso ---")
        print("1. Simular acceso")
        print("2. Volver al menú principal")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            while True:
                print("\nSimulación de intento de acceso:")

                # Solicitar datos al usuario
                tiene_membresia = input("¿Tiene membresía válida? (s/n): ").strip().lower() == 's'
                es_empleado = input("¿Es empleado? (s/n): ").strip().lower() == 's'
                horario_atencion = input("¿Es horario de atención? (s/n): ").strip().lower() == 's'

                # Evaluar condiciones
                if (tiene_membresia and horario_atencion) or es_empleado:
                    print("✅ Acceso PERMITIDO.")
                else:
                    print("❌ Acceso DENEGADO.")

                repetir = input("\n¿Deseas simular otro intento de acceso? (s/n): ").strip().lower()
                if repetir != 's':
                    break

        elif opcion == '2':
            break

        elif opcion == '3':
            print("👋 Saliendo del sistema...")
            exit()

        else:
            print("❌ Opción no válida. Intenta de nuevo.")

def menu_principal():
    while True:
        print("\n===== Menú Principal del Sistema de Control de Acceso =====")
        print("1. Control de acceso a tienda")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            controlar_acceso_tienda()
        elif opcion == '2':
            print("👋 Gracias por usar el sistema. Hasta luego.")
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")

# Ejecutar menú principal
menu_principal()
