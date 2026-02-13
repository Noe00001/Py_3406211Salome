# 2. Área de un rectángulo: Solicitar la base y la altura de un rectángulo. Calcular y mostrar el área correspondiente.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:

        x = int(input("Ingresar base"))
        y = int(input("Ingresar altura"))

        area = x * y

        print("El resultado de la multiplicacion es: ", area)
        
    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()