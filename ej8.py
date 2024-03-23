# calculos.py
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
