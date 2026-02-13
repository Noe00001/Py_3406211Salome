# 24. Factura de servicios públicos: Solicitar el consumo de agua en metros cúbicos y el valor por metro cúbico. Calcular el valor total de la factura.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:



        consumo_agua = float(input("Ingrese el consumo de agua en metros cúbicos: "))
        valor_por_metro = float(input("Ingrese el valor por metro cúbico: "))

        valor_total_factura = consumo_agua * valor_por_metro

        print("El valor total de la factura de servicios públicos es:", valor_total_factura)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()
