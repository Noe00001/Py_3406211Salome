# 25. Venta diaria de un almacén: Solicitar el número de ventas realizadas en el día y el valor de cada venta. Calcular el total vendido y el promedio por venta.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:



        num_ventas = int(input("Ingrese el número de ventas realizadas en el día: "))

        total_vendido = 0

        for i in range(num_ventas):
            valor_venta = float(input("Ingrese el valor de la venta #" + str(i + 1) + ": "))
            total_vendido += valor_venta

        promedio_venta = total_vendido / num_ventas if num_ventas > 0 else 0

        print("El total vendido en el día es:", total_vendido)
        print("El promedio por venta es:", promedio_venta)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()

