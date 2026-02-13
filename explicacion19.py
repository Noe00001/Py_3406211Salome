# 19. Conversión de moneda: Solicitar un valor en pesos colombianos y convertirlo a dólares, usando una tasa de cambio ingresada por el usuario.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:



        valor_pesos = float(input("Ingrese el valor en pesos colombianos: "))
        tasa_cambio = float(input("Ingrese la tasa de cambio (pesos por dólar): "))

        valor_dolares = valor_pesos / tasa_cambio

        print("El valor en dólares es:", valor_dolares)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()
