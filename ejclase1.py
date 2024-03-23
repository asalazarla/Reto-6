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
