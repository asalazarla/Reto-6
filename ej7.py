import statistics

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    return statistics.median(numeros)

def calcular_promedio_multiplicativo(numeros):
    producto = 1
    for num in numeros:
        producto *= num
    return producto ** (1 / len(numeros))

def ordenar_ascendente(numeros):
    return sorted(numeros)

def ordenar_descendente(numeros):
    return sorted(numeros, reverse=True)

def potencia_mayor_al_menor(numeros):
    numeros.sort()
    return numeros[-1] ** numeros[0]

def raiz_cubica_del_menor(numeros):
    numeros.sort()
    return numeros[0] ** (1/3)

# Solicitar 5 números al usuario
numeros = []
for i in range(5):
    num = float(input("Ingrese el número {}: ".format(i+1)))
    numeros.append(num)

# Calcular y mostrar los resultados
print("El promedio es:", calcular_promedio(numeros))
print("La mediana es:", calcular_mediana(numeros))
print("El promedio multiplicativo es:", calcular_promedio_multiplicativo(numeros))
print("Números ordenados de forma ascendente:", ordenar_ascendente(numeros))
print("Números ordenados de forma descendente:", ordenar_descendente(numeros))
print("Potencia del mayor número elevado al menor número:", potencia_mayor_al_menor(numeros))
print("Raíz cúbica del menor número:", raiz_cubica_del_menor(numeros))
