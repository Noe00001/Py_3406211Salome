# 20. Cálculo de intereses simples: Solicitar el capital, la tasa de interés y el tiempo en meses. Calcular el interés simple y el valor total a pagar.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:



        capital = float(input("Ingrese el capital: "))
        tasa_interes = float(input("Ingrese la tasa de interés (% anual): "))
        tiempo_meses = int(input("Ingrese el tiempo en meses: "))

        interes_simple = (capital * tasa_interes * tiempo_meses) / 1200
        total_pagar = capital + interes_simple

        print("El interés simple es:", interes_simple)
        print("El valor total a pagar es:", total_pagar)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()
