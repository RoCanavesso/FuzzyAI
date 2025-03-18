import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

# Definição das variáveis fuzzy
calorias = ctrl.Antecedent(np.arange(1000, 5000, 100), 'calorias')

# Definição das funções de pertinência
# Triangular
calorias['pouco_tri'] = fuzz.trimf(calorias.universe, [1000, 1500, 2000])
calorias['moderado_tri'] = fuzz.trimf(calorias.universe, [2000, 2500, 3000])
calorias['muito_tri'] = fuzz.trimf(calorias.universe, [3000, 4000, 5000])

# Gaussiana
calorias['pouco_gauss'] = fuzz.gaussmf(calorias.universe, 1500, 300)
calorias['moderado_gauss'] = fuzz.gaussmf(calorias.universe, 2500, 300)
calorias['muito_gauss'] = fuzz.gaussmf(calorias.universe, 4000, 500)

# Trapezoidal
calorias['pouco_trap'] = fuzz.trapmf(calorias.universe, [1000, 1200, 1800, 2000])
calorias['moderado_trap'] = fuzz.trapmf(calorias.universe, [2000, 2200, 2800, 3000])
calorias['muito_trap'] = fuzz.trapmf(calorias.universe, [3000, 3500, 4500, 5000])

# Criando os gráficos personalizados para cada tipo de função
x = np.arange(1000, 5000, 100)

# Triangular
plt.figure(figsize=(10, 6))
plt.title("Funções de Pertinência - Triangular")
plt.plot(x, fuzz.trimf(x, [1000, 1500, 2000]), label='Pouco')
plt.plot(x, fuzz.trimf(x, [2000, 2500, 3000]), label='Moderado')
plt.plot(x, fuzz.trimf(x, [3000, 4000, 5000]), label='Muito')
plt.xlabel("Consumo de Calorias")
plt.ylabel("Grau de Pertinência")
plt.legend()
plt.grid()
plt.show()

# Gaussiana
plt.figure(figsize=(10, 6))
plt.title("Funções de Pertinência - Gaussiana")
plt.plot(x, fuzz.gaussmf(x, 1500, 300), label='Pouco')
plt.plot(x, fuzz.gaussmf(x, 2500, 300), label='Moderado')
plt.plot(x, fuzz.gaussmf(x, 4000, 500), label='Muito')
plt.xlabel("Consumo de Calorias")
plt.ylabel("Grau de Pertinência")
plt.legend()
plt.grid()
plt.show()

# Trapezoidal
plt.figure(figsize=(10, 6))
plt.title("Funções de Pertinência - Trapezoidal")
plt.plot(x, fuzz.trapmf(x, [1000, 1200, 1800, 2000]), label='Pouco')
plt.plot(x, fuzz.trapmf(x, [2000, 2200, 2800, 3000]), label='Moderado')
plt.plot(x, fuzz.trapmf(x, [3000, 3500, 4500, 5000]), label='Muito')
plt.xlabel("Consumo de Calorias")
plt.ylabel("Grau de Pertinência")
plt.legend()
plt.grid()
plt.show()
