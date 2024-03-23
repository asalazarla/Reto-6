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