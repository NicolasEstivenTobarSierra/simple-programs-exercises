# Pedir al usuario que ingrese 4 notas
note1 = float(input("Enter the first note: "))  # Primera nota
note2 = float(input("Enter the second note: "))  # Segunda nota
note3 = float(input("Enter the third note: "))   # Tercera nota
note4 = float(input("Enter the quarter note: "))    # Cuarta nota

# Calcular el promedio
promedio = (note1 + note2 + note3 + note4) / 4  # Sumar las notas y dividir entre 4

# Mostrar el resultado
print("El promedio es:", promedio)  # Imprimir el promedio
