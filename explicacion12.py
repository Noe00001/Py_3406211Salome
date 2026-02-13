# 12. Comisión escalonada: Solicitar el valor de ventas mensuales. Si las ventas son mayores a $1.000.000, la comisión es del 10%; de lo contrario, es del 5%. Mostrar la comisión.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:



        ventas_mensuales = float(input("Ingrese el valor de ventas mensuales: "))
        if ventas_mensuales > 1000000:

            comision = ventas_mensuales * 0.10
        else:
            comision = ventas_mensuales * 0.05
        print("La comisión por ventas es:", comision)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()