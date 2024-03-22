# Reto-6

1. Dado la figura de la imagen, desarrolle:
[![img-1.png](https://i.postimg.cc/nVBj1Lc6/img-1.png)](https://postimg.cc/XXNYj458)
- Una función matemática para calcular el volumen y el área superficial.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
- Revise como utilizar el valor de pi usando import math y math.pi

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
def calcular_peso_carne(N, M, K):
    # Calcular el peso total de las gallinas
    peso_gallinas = N * 6

    # Calcular el peso total de los gallos
    peso_gallos = M * 7

    # Calcular el peso total de los pollitos
    peso_pollitos = K * 1

    # Calcular el peso total de todas las aves
    peso_total = peso_gallinas + peso_gallos + peso_pollitos

    return peso_total

# Ejemplo de uso de la función
cantidad_carne = calcular_peso_carne(10, 5, 20)
print("La cantidad total de carne de aves es:", cantidad_carne, "kilos")
```

4.Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
def calcular_vueltas(P, M, H, B):
    # Calcular el costo total de los productos
    costo_total = P * 300 + M * 3300 + H * 350

    # Calcular las vueltas o lo que se debe
    vueltas = B - costo_total

    return vueltas

# Ejemplo de uso del programa
P = int(input("Ingrese la cantidad de panes a comprar: "))
M = int(input("Ingrese la cantidad de bolsas de leche a comprar: "))
H = int(input("Ingrese la cantidad de huevos a comprar: "))
B = int(input("Ingrese el valor del billete en pesos: "))

resultado = calcular_vueltas(P, M, H, B)

if resultado >= 0:
    print("Las vueltas son:", resultado, "pesos")
else:
    print("Debe:", abs(resultado), "pesos")
```

5.Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
```python
def calcular_valor_prestamo(C, i, n):
    # Fórmula del interés compuesto: A = C * (1 + i)^n
    valor_prestamo = C * (1 + i)**n
    return valor_prestamo

# Ejemplo de uso del programa
C = float(input("Ingrese el monto del préstamo: "))
i = float(input("Ingrese la tasa de interés anual (en decimal): "))
n = int(input("Ingrese el número de meses: "))

valor_final = calcular_valor_prestamo(C, i, n)
print("El valor final del préstamo después de", n, "meses es:", valor_final)

```

6.El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```python
def calcular_contagiados(C, D):
    # El número de contagiados se duplica cada día
    contagiados_totales = C * (2 ** D)
    return contagiados_totales

# Ejemplo de uso del programa
C = int(input("Ingrese el número actual de contagiados en NuncaLandia: "))
D = int(input("Ingrese el número de días a partir de hoy: "))

contagiados_totales = calcular_contagiados(C, D)
print("El número total de personas contagiadas después de", D, "días será:", contagiados_totales)

```

7.Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

- El promedio
- La mediana
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
- Ordenar los números de forma ascendente
- Ordenar los números de forma descendente
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número

```python
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

```

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.



10. Consultar qué es y cómo funciona pip en python.

11. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

