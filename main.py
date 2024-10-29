# Solicitar las notas de los dos primeros certámenes y la nota de laboratorio
C1 = float(input("Ingresa la nota del primer certamen: "))
C2 = float(input("Ingresa la nota del segundo certamen: "))
NL = float(input("Ingresa la nota de laboratorio: "))

# Nota final que se desea alcanzar
NF_deseada = 60

# Calcular la nota que necesita en el tercer certamen
# NF = NC * 0.7 + NL * 0.3
# NC = (C1 + C2 + C3) / 3

# Rearreglando la fórmula para encontrar C3:
# C3 = (NF_deseada - NL * 0.3) / 0.7 * 3 - C1 - C2

# Calcular C3
C3_necesaria = ((NF_deseada - NL * 0.3) / 0.7) * 3 - C1 - C2

# Mostrar el resultado
print(f"Necesitas una nota de {C3_necesaria:.2f} en el tercer certamen para aprobar el ramo.")