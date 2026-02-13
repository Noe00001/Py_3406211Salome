# 15. Mayor de dos números: Solicitar dos números enteros y mostrar cuál de ellos es mayor o si son iguales.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:


        numero1 = int(input("Ingrese el primer número entero: "))
        numero2 = int(input("Ingrese el segundo número entero: "))

        if numero1 > numero2:
            print("El número mayor es:", numero1)
        elif numero2 > numero1:
            print("El número mayor es:", numero2)
        else:
            print("Los números son iguales.")
    
    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()
