# 14. Nota final ponderada: Solicitar la nota de tres actividades: talleres (30%), examen parcial (30%) y examen final (40%). Calcular la nota definitiva.

print("===========================")
print("Taller 1 algoritmos y basicos")
print("By Salomé López Estrada") 
print("Actividades")  
print("============================")

def explicacion1():
    try:


        talleres = float(input("Ingrese la nota de los talleres (30%): "))
        examen_parcial = float(input("Ingrese la nota del examen parcial (30%): "))
        examen_final = float(input("Ingrese la nota del examen final (40%): "))

        nota_definitiva = (talleres * 0.30) + (examen_parcial * 0.30) + (examen_final * 0.40)

        print("La nota definitiva es:", nota_definitiva)

    except ValueError:
        print("Error: Por favor ingresa numero valido.")
        
if __name__ == "__main__":
    explicacion1()