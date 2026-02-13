# 11. Comisión por ventas: Solicitar el valor total de ventas realizadas por un vendedor. Calcular una comisión del 5% y mostrar el total a recibir.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:




        ventas = float(input("Ingrese el valor total de ventas realizadas por el vendedor: "))

        comision = ventas * 0.05
        total_a_recibir = ventas + comision

        print("La comisión por ventas es:", comision)
        print("El total a recibir por el vendedor es:", total_a_recibir)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()
