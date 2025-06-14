import matplotlib.pyplot as plt
import numpy as np

# 1. Генерация случайных данных
np.random.seed(0)  # чтобы результаты были одинаковыми при каждом запуске
n = 50  # количество людей

height = np.random.normal(170, 10, n)  # рост: среднее 170, разброс ±10
weight = np.random.normal(65, 15, n)   # вес: среднее 65, разброс ±15
age = np.random.randint(18, 60, n)     # возраст: от 18 до 60
gender = np.random.choice(['M', 'F'], n)  # случайный пол: M (муж) или F (жен)

# 2. Преобразуем пол в числа, чтобы можно было использовать цвета
gender_colors = []  # список цветов
for g in gender:
    if g == 'M':
        gender_colors.append('blue')  # мужчины - синие
    else:
        gender_colors.append('red')   # женщины - красные

# 3. Построение scatter plot
plt.figure(figsize=(8, 6))  # размер окна
plt.scatter(
    height, weight,     # X и Y оси
    s=age,              # размер точки — возраст
    c=gender_colors,    # цвет по полу
    alpha=0.6,          # прозрачность точек
    edgecolors='black'  # обводка для контраста
)

# 4. Подписи и оформление
plt.xlabel('Рост (см)')
plt.ylabel('Вес (кг)')
plt.title('Рост vs Вес (размер = возраст, цвет = пол)')
plt.grid(True)
plt.show()