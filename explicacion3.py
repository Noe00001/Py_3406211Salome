# 3. Conversión de temperatura: Solicitar una temperatura en grados Celsius y convertirla a grados Fahrenheit.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:

        Celcius = float(input("temperatura en Celsius: "))

        F = (Celcius * 1.8) + 32

        print("El resultado de la conversion es", F)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()