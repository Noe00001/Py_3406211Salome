# 16. Número par o impar: Solicitar un número entero e indicar si es par o impar.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:


        numero = int(input("Ingrese un número entero: "))

        if numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()