# Solicitar al usuario que ingrese un entero de tres dígitos
numero = input("Ingresa un número entero de tres dígitos: ")

# Verificar que el número tenga exactamente tres dígitos
if len(numero) == 3 and numero.isdigit():
    # Invertir los dígitos
    numero_invertido = numero[2] + numero[1] + numero[0]
    
    # Mostrar el resultado
    print("El número con los dígitos en orden inverso es:", numero_invertido)
else:
    print("Por favor, asegúrate de ingresar un número entero de tres dígitos.")