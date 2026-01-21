import json
import os

def task() -> float:

    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'input.json')

    with open(file_path, 'r') as f:
        data = json.load(f)

    # Переменная для накопления суммы
    total_sum = 0.0

    # Проходим по всем элементам в списке
    for item in data:
        score = item.get('score', 0)
        weight = item.get('weight', 0)

        # Вычисляем произведение и добавляем к общей сумме
        total_sum += score * weight

    # Округляем результат до 3 знаков после запятой и возвращаем
    # round() возвращает число с плавающей точкой
    return round(total_sum, 3)

print(task())
