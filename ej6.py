def calcular_contagiados(C, D):
    # El número de contagiados se duplica cada día
    contagiados_totales = C * (2 ** D)
    return contagiados_totales

# Ejemplo de uso del programa
C = int(input("Ingrese el número actual de contagiados en NuncaLandia: "))
D = int(input("Ingrese el número de días a partir de hoy: "))

contagiados_totales = calcular_contagiados(C, D)
print("El número total de personas contagiadas después de", D, "días será:", contagiados_totales)

