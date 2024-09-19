import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Константи
alpha = 0.1  # Коефіцієнт народжуваності жертв
beta = 0.02  # Коефіцієнт смертності жертв через хижаків
delta = 0.01 # Коефіцієнт народжуваності хижаків через жертв
gamma = 0.1  # Коефіцієнт смертності хижаків

# Початкові умови: [кількість жертв, кількість хижаків]
initial_conditions = [40, 9]

# Функція, яка описує рівняння системи хижак-жертва
def lotka_volterra(y, t, alpha, beta, delta, gamma):
    prey, predator = y
    dydt = [alpha * prey - beta * prey * predator,
            delta * prey * predator - gamma * predator]
    return dydt

# Часовий інтервал
t = np.linspace(0, 200, 1000)

# Розв'язання диференціальних рівнянь
solution = odeint(lotka_volterra, initial_conditions, t, args=(alpha, beta, delta, gamma))

# Витягування популяцій з розв'язку
prey_population = solution[:, 0]
predator_population = solution[:, 1]

# Візуалізація результатів
plt.figure(figsize=(10, 5))
plt.plot(t, prey_population, label='Жертви')
plt.plot(t, predator_population, label='Хижаки')
plt.xlabel('Час')
plt.ylabel('Популяція')
plt.title('Модель Лотки-Вольтерри')
plt.legend()
plt.grid(True)
plt.show()