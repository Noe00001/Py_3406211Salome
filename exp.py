print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")


import math

radio = float(input ("Ingrese el radio de un circulo" ))

area = math.pi * math.pow(radio, 2)

perimetro = 2 * math.pi * radio

print("Area: ", round(area, 2))
print("Perimetro", round(perimetro, 2))