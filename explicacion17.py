# 17. Edad de una persona: Solicitar el año de nacimiento y el año actual. Calcular y mostrar la edad de la persona.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:



        a_nacimiento = int(input("Ingrese el año de nacimiento: "))
        a_actual = int(input("Ingrese el año actual: "))

        edad = a_actual - a_nacimiento

        print("La edad de la persona es:", edad)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()
