# Compra de varios productos: Solicitar la cantidad de productos comprados y el precio de cada uno. Calcular el total de la compra.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:




        cantidad_productos = int(input("Ingrese la cantidad de productos comprados: "))
        precio_producto = float(input("Ingrese el precio de cada producto: ")) 

        total_compra = cantidad_productos * precio_producto

        print("El total de la compra es:", total_compra)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()