import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Константи
g = 9.81  # Прискорення вільного падіння, м/с^2
L = 1.0   # Довжина маятника, м
b = 0.05  # Коефіцієнт демпфування

# Початкові умови: [кут, кутова швидкість]
theta0 = [np.pi / 4, 0.0]

# Функція, яка описує рівняння руху маятника
def pendulum_equations(y, t, b, g, L):
    theta, omega = y
    dydt = [omega, -b * omega - (g / L) * np.sin(theta)]
    return dydt

# Часовий інтервал
t = np.linspace(0, 10, 250)

# Розв'язання диференціальних рівнянь
solution = odeint(pendulum_equations, theta0, t, args=(b, g, L))

# Витягування кутів з розв'язку
theta = solution[:, 0]

# Візуалізація результатів
plt.figure(figsize=(10, 5))
plt.plot(t, theta, label='Кут (рад)')
plt.xlabel('Час (с)')
plt.ylabel('Кут (рад)')
plt.title('Рух маятника')
plt.legend()
plt.grid(True)
plt.show()