# 13. Promedio de notas: Solicitar tres notas de un estudiante. Calcular el promedio e indicar si aprueba (promedio mayor o igual a 3.0).

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")


def explicacion1():
    try:


        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))

        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 3.0:

            print("El estudiante aprueba con un promedio de:", promedio)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()