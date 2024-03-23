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
