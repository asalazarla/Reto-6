# Reto-6

1. Dado la figura de la imagen, desarrolle:
   
[![img-1.png](https://i.postimg.cc/nVBj1Lc6/img-1.png)](https://postimg.cc/XXNYj458)
- Una función matemática para calcular el volumen y el área superficial.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
- Revise como utilizar el valor de pi usando import math y math.
```python

import math

def volumen_esferoide(r1, r2):
    return (4/3) * math.pi * r1**2 * r2

def area_esferoide(r1, r2):
    if r1 > r2:
        # Esferoide oblato
        e = math.sqrt(1 - (r2**2 / r1**2))
    else:
        # Esferoide prolate
        e = math.sqrt((r2**2 / r1**2) - 1)
    if r1 != r2:
        factor = (1 - e**2) / e * math.asinh(e)
    else:
        factor = 0
    return 2 * math.pi * r1**2 * (1 + factor)

def volumen_cono(r, h):
    return (1/3) * math.pi * r**2 * h

def area_cono(r, h):
    return math.pi * r * math.sqrt(r**2 + h**2)

# Uso de funciones
r1 = float(input("Ingrese r1 para el esferoide: "))
r2 = float(input("Ingrese r2 para el esferoide: "))
h = float(input("Ingrese h para el cono: "))

print(f"Volumen del esferoide: {volumen_esferoide(r1, r2)}")
print(f"Área superficial del esferoide: {area_esferoide(r1, r2)}")
print(f"Volumen del cono: {volumen_cono(r2, h)}")
print(f"Área superficial del cono (sin base): {area_cono(r2, h)}")


```
2. Dado la figura de la imagen, desarrolle:

   
[![img-2.png](https://i.postimg.cc/N0WdX0pd/img-2.png)](https://postimg.cc/8FmdQT8v)

- Una función matemática para calcular el área y el perímetro.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
- Revise como utilizar el valor de pi usando import math y math.pi
  
```python
import math

def calcular_area(a, b, r):
    area_rectangulo = a * b
    area_circulo_completo = math.pi * r**2
    return area_rectangulo + area_circulo_completo

def calcular_perimetro(a, b, r):
    perimetro_rectangulo = 2 * (a + b)
    circunferencia_circulo = 2 * math.pi * r
    return perimetro_rectangulo - 2 * b + circunferencia_circulo

# Uso de las funciones
r = float(input("Ingrese el radio r de los semicírculos: "))
a = float(input("Ingrese el largo a del rectángulo: "))
b = float(input("Ingrese el ancho b del rectángulo: "))

area = calcular_area(a, b, r)
perimetro = calcular_perimetro(a, b, r)

print(f"El área de la figura es: {area}")
print(f"El perímetro de la figura es: {perimetro}")
```

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

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.


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

5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

   
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

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

   
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

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

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

```python

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
```

El archivo está adjunto con los demás.

9. Consultar qué es y cómo funciona pip en python.

PIP es un sistema de gestión de paquetes para Python que permite instalar, actualizar y manejar bibliotecas y dependencias que no están incluidas en la biblioteca estándar de Python.Cuando se instala un paquete con PIP, este busca el paquete en el Python Package Index (PyPI), descarga el paquete y sus dependencias, y los instala en el sistema.
PyPI es un repositorio de software para el lenguaje de programación Python que ayuda a los usuarios a encontrar y a instalar software desarrollado y compartido por la comunidad de Python. pip también maneja la compilación de algunos paquetes si es necesario, gestiona versiones y asegura que se instalen las versiones de los paquetes compatibles entre sí, basándose en los requerimientos de cada paquete.

10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

Existen diversos paquetes, con distintas funciones y se instalan proporcionando el comando pip install seguido del nombre del paquete, como por ejemplo:

- Desarrollo web:
Flask: un micro framework para desarrollo web en Python.
```python
pip install Flask
```

- Análisis de datos:
Matplotlib: una biblioteca de trazado para la visualización de datos en Python.
```python
pip install matplotlib
```

Scikit-learn: herramientas simples y eficientes para el análisis de datos y la minería de datos.
```python
pip install scikit-learn
```

-Automatización y Sripts:
Selenium: una herramienta para automatizar navegadores web.
```python
pip install seleniumn
```

Beautiful Soup: una biblioteca que facilita raspar información de páginas web.
pip install scikit-learn
``````python
pip install beautifulsoup4
```
Estos son solo algunos de los miles de los módulos de python. ;)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Además, para cumplir el retp se requiere hacer los ejercicios propuestos en clase.

- Realice un programa que ingrese dos masas y la distancia que las separa y calcule la fuerza de gravedad entre ellas. Resuelva usando una función.

```python
G : float = 6.67384e-11 # Constante de Cavendish [Nm^2/kg^2]
```

```python
# Definición de la función para calcular la fuerza de gravedad
def calcular_fuerza_gravitacional(m1, m2, r):
    G = 6.67384e-11  # Constante de gravitación universal
    return G * m1 * m2 / r**2

# Función principal
def main():
    m1 = float(input("Ingrese la masa del primer objeto (en kilogramos): "))
    m2 = float(input("Ingrese la masa del segundo objeto (en kilogramos): "))
    r = float(input("Ingrese la distancia entre los objetos (en metros): "))
    
    fuerza = calcular_fuerza_gravitacional(m1, m2, r)
    print(f"La fuerza de gravedad entre los objetos es de {fuerza} Newtons")

# Punto de entrada del script
if __name__ == "__main__":
    main()
```

- Uno de los módulos que trae python es math, hacer un porgrama en Python importando math y usar 5 de las funciones incluidas en este módulo.

```python
def elevar_cuadrado(x: float) -> float:
    return x**2

def sumar_dos_numeros(x: float, y: float) -> float:
    return x + y

def main():
    x = float(input("Ingrese un numero real para x: "))
    x_squared = elevar_cuadrado(x)
    print("El cuadrado de " + str(x) + " es " + str(x_squared))

    y = float(input("Ingrese un numero real para y: "))
    suma = sumar_dos_numeros(x, y)
    print("La suma de " + str(x) + " y " + str(y) + " es " + str(suma))

if __name__ == "__main__":
    main()
```

