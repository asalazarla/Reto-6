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
