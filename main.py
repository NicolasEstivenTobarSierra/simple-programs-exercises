# Solicitar la hora actual (en formato de 24 horas)
hora_actual = int(input("Ingresa la hora actual (0-23): "))
# Solicitar el número de horas a sumar
horas_a_sumar = int(input("Ingresa el número de horas a sumar: "))

# Calcular la nueva hora
nueva_hora = (hora_actual + horas_a_sumar) % 24

# Mostrar el resultado
print(f"La hora después de {horas_a_sumar} horas será: {nueva_hora}")