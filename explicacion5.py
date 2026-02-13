#Salario con horas extra: Solicitar horas trabajadas y valor por hora. Si el empleado trabajó más de 40 horas, las horas adicionales se pagan al 150%. Calcular el salario total.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:



        horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas en la semana:"))
        valor_por_hora = float(input("Ingrese el valor por hora:"))

        horas_extra = horas_trabajadas - 40
        pago_normal = 40* valor_por_hora
        pago_extra = horas_extra * (valor_por_hora * 1.5)

        pago_normal = horas_extra * valor_por_hora 
        pago_extra = 0

        salario_total = pago_normal + pago_extra

        print("salario_total", salario_total)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()