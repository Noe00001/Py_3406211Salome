# Venta con descuento por porcentaje: Solicitar el precio de un producto y el porcentaje de descuento. Calcular y mostrar el valor del descuento y el precio final.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:


        precio = float(input("Ingrese el precio del producto: "))
        descuento_porcentaje = float(input("Ingrese el porcentaje de descuento: "))


        descuento = precio * (descuento_porcentaje / 100)
        precio_final = precio - descuento


        print("El valor del descuento es:", descuento)
        print("El precio final a pagar es:", precio_final)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()