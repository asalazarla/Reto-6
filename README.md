# Reto-6

1. Dado la figura de la imagen, desarrolle:
[![img-1.png](https://i.postimg.cc/nVBj1Lc6/img-1.png)](https://postimg.cc/XXNYj458)
- Una función matemática para calcular el volumen y el área superficial.
- Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
- Revise como utilizar el valor de pi usando import math y math.pi

```code
3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```code
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

```code
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
