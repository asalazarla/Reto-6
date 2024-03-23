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

