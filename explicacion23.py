# 23. Costo de envío: Solicitar el peso de un paquete. Si pesa hasta 5 kg, el envío cuesta $10.000; si pesa más, cuesta $20.000. Mostrar el valor del envío.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:


        peso_paquete = float(input("Ingrese el peso del paquete en kg: "))

        if peso_paquete <= 5:
            costo_envio = 10000
        else:
            costo_envio = 20000

        print("El costo de envío es:", costo_envio)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()