# 18. Clasificación por edad: Solicitar la edad de una persona e indicar si es menor de edad, adulto o adulto mayor.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:



        edad = int(input("Ingrese la edad de la persona: "))

        if edad < 18:
            print("La persona es menor de edad.")
        elif edad < 60:
            print("La persona es adulta.")
        else:
            print("La persona es adulto mayor.")
    
    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()