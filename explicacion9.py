#Venta con IVA: Solicitar el valor de una venta sin impuestos. Calcular el IVA (19%) y mostrar el valor del IVA y el total con impuesto incluido.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:



        venta_sin_iva = float(input("Ingrese el valor de la venta sin impuestos: "))

        iva = venta_sin_iva * 0.19
        total_con_iva = venta_sin_iva + iva

        print("El valor del IVA es:", iva)
        print("El total con IVA incluido es:", total_con_iva)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()