import math

# Definición de constantes
M = 47  # Masa del huevo en gramos para un huevo pequeño
rho = 1.038  # Densidad en g/cm³
c = 3.7  # Capacidad calorífica específica en J/(g·K)
K = 5.4e-3  # Conductividad térmica en W/(cm·K)
Tw = 100  # Temperatura de ebullición del agua en °C
Ty = 70  # Temperatura máxima de la yema en °C

# Solicitar la temperatura original del huevo
To = float(input("Ingresa la temperatura original del huevo (en °C): "))

# Calcular el tiempo usando la fórmula
t = (M**(2/3) * c * rho**(1/3) * K * math.pi**2 * ((4 * math.pi / 3)**(2/3)) *
     math.log((0.76 * To - Tw) / (Ty - Tw)))

# Mostrar el resultado
print(f"El tiempo que toma al centro de la yema alcanzar {Ty}°C es: {t:.2f} segundos.")