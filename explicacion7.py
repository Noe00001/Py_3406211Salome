# Venta con descuento fijo: Solicitar el valor total de una compra. Si la compra supera los $200.000, aplicar un descuento del 10%. Mostrar el valor final a pagar

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:


        compra = float(input ("Ingrese valor de la compra"))

        if compra >= 200000 :
            descuento = compra * 0.10
            total = compra - descuento
            print("Se aplico un descuento del 10% FELICIDADES WIWIWIWIWI")

        else:
            total = compra
            print("No se cumplio el requisito")
            print("El valor total a pagar es:", total)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()
