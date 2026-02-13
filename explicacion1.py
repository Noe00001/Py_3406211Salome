#Entradas

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")


def explicacion1():
    try:


        x = int(input("Ingresa el primer numero entero: " ))
        y = int(input("Ingresa el segundo numero entero: " ))
        z = int(input("Ingresa el tercer numero entero: " ))

        #Calculos/Proceso
        sum = x + y + z
        average = sum / 3 

        #Salidas
        print("La suma total es:", sum)
        print("El promedio es:", int(average))
    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()