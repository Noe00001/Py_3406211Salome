# 21. Cálculo de intereses compuestos: Solicitar el capital inicial, la tasa de interés y el número de períodos. Calcular el monto final.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")


def explicacion1():
    try:


        capital_inicial = float(input("Ingrese el capital inicial: "))
        tasa_interes = float(input("Ingrese la tasa de interés (% anual): "))
        num_periodos = int(input("Ingrese el número de períodos (años): "))

        monto_final = capital_inicial * (1 + tasa_interes / 100) ** num_periodos

        print("El monto final después de", num_periodos, "años es:", monto_final)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()
