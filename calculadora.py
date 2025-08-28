def mostrar_menu():
    print("\n--- MENÚ DE LA CALCULADORA ---")
    print("1. Mensaje de bienvenida")
    print("2. Usar la calculadora")
    print("3. Reiniciar calculadora")
    print("4. Salir")

def mensaje_bienvenida():
    print("\n¡Bienvenido a la calculadora simple!")
    print("Esta calculadora permite realizar las siguientes operaciones:")
    print("- Suma (+)")
    print("- Resta (-)")
    print("- Multiplicación (*)")
    print("- División (/)")
    print("Puede realizar múltiples operaciones hasta que decida salir.\n")

def usar_calculadora():
    while True:
        try:
            num1 = float(input("Ingrese el primer número (o 's' para salir): "))
        except ValueError:
            entrada = input("¿Desea salir de la calculadora? (s/n): ").strip().lower()
            if entrada == "s":
                break
            else:
                continue

        try:
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
            continue

        operacion = input("Ingrese la operación (+, -, *, /): ").strip()

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
                continue
            resultado = num1 / num2
        else:
            print("Operación no válida.")
            continue

        print(f"Resultado: {resultado}")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            mensaje_bienvenida()
        elif opcion == "2":
            usar_calculadora()
        elif opcion == "3":
            print("\nReiniciando calculadora...\n")
        elif opcion == "4":
            print("\nGracias por usar la calculadora. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    calculadora()
