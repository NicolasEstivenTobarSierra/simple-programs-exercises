import math

# Solicitar al usuario que ingrese las longitudes de los catetos
a = float(input("Ingresa la longitud del cateto a: "))
b = float(input("Ingresa la longitud del cateto b: "))

# Calcular la hipotenusa usando el teorema de Pitágoras
c = math.sqrt(a**2 + b**2)

# Mostrar el resultado
print(f"La longitud de la hipotenusa c es: {c}")