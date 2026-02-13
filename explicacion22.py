# 22. Control de inventario: Solicitar la cantidad inicial de un producto en inventario, la cantidad vendida y la cantidad recibida. Calcular el inventario final.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:



        cantidad_inicial = int(input("Ingrese la cantidad inicial de producto en inventario: "))
        cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
        cantidad_recibida = int(input("Ingrese la cantidad recibida: "))

        inventario_final = cantidad_inicial - cantidad_vendida + cantidad_recibida

        print("El inventario final es:", inventario_final)


    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()