# Salario semanal: Solicitar la cantidad de horas trabajadas en la semana y el valor por hora. Calcular y mostrar el salario semanal.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:


        horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas en la semana: "))
        valor_por_hora = float(input("ingrese el valor por hora: "))

        salario_semanal = horas_trabajadas * valor_por_hora

        print("El salario semanal es:", salario_semanal)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()