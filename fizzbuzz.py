def mostrar_menu():
    print("\n--- MENÚ DEL JUEGO FIZZBUZZ ---")
    print("1. Mensaje de bienvenida")
    print("2. Ejecutar FizzBuzz (1 al 100)")
    print("3. Reiniciar ejercicio")
    print("4. Salir")

def mensaje_bienvenida():
    print("\n¡Bienvenido al Juego FizzBuzz!")
    print("Este programa recorre los números del 1 al 100.")
    print("Por cada número:")
    print("- Imprime 'Fizz' si es divisible por 3.")
    print("- Imprime 'Buzz' si es divisible por 5.")
    print("- Imprime 'FizzBuzz' si es divisible por ambos.")
    print("- Si no cumple ninguna condición, imprime el número.\n")

def ejecutar_fizzbuzz():
    print("\n--- Ejecutando FizzBuzz ---")
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def juego_fizzbuzz():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            mensaje_bienvenida()
        elif opcion == "2":
            ejecutar_fizzbuzz()
        elif opcion == "3":
            print("\nReiniciando el ejercicio FizzBuzz...\n")
        elif opcion == "4":
            print("\nGracias por jugar FizzBuzz. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el juego
if __name__ == "__main__":
    juego_fizzbuzz()
