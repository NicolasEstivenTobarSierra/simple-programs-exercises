# Solicitar al usuario que ingrese un número real
numero_real = float(input("Ingresa un número real: "))

# Calcular la parte decimal
parte_decimal = numero_real - int(numero_real)

# Mostrar el resultado
print(f"La parte decimal de {numero_real} es: {parte_decimal}")