#Total de una venta: Solicitar el nombre del producto, el precio unitario y la cantidad comprada. Calcular y mostrar el valor total a pagar.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:

        producto = input("Ingrese el nombre del producto")
        p = int(input("Ingrese el precio"))
        c = int(input("Ingrese la cantidad comprada"))

        total_pagar = p * c

        print("El total a pagar es:", total_pagar )

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()