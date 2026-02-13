
import os # Inportamos el módulo os para manejar operaciones del sistema operativo (Archivos, directorios, rutas, variables de entorno, etc.)
import sys # Importamos el módulo sys para acceder a funciones y variables relacionadas con el intérprete de Python (Argumentos de línea de comandos, salida estándar, manejo de excepciones, etc.)
import subprocess # Importamos el módulo subprocess para ejecutar comandos del sistema operativo y manejar procesos externos (Ejecutar programas, capturar salida, etc.)



while True:
    #encabezado
    print("===========================")
    print("Taller 1 algoritmos y basicos")
    print("By Salomé López Estrada") 
    print("Menu Principal")  
    print("============================")

    for i in range(1, 26):
        print(f"{i}. Ejecutar Algoritmo {i}")
    print("0. Salir\n")

    opcion = input("Seleccione una opción: ")
    if opcion == "0":
        print("Saliendo del programa...")
        break

    if opcion.isdigit() and 1 <= int(opcion) <= 25:
        archivo = f"ex{opcion}.py"


        if os.path.exists(archivo):
            subprocess.run([sys.executable, archivo])
        else:
            print(f"Voló {archivo} no existe.")
    else:
            print("Opción no válida.")

    input("\nPresione Enter para continuar...") 


