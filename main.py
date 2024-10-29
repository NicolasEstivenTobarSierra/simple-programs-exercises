# Solicitar al usuario que ingrese un entero de tres dígitos
number = input("Enter a three-digit integer: ")

# Verificar que el número tenga exactamente tres dígitos
if len(number) == 3 and number.isdigit():
    # Invertir los dígitos
    numero_invertido = number[2] + number[1] + number[0]
    
    # Mostrar el resultado
    print("The number with the digits in reverse order is:", numero_invertido)
else:
    print("Please, make sure to enter a three-digit number")