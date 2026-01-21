# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    # Разделяем строки на списки участников с помощью метода split()
    participants1 = group1.split(separator)  # Метод строки для разделения по разделителю
    participants2 = group2.split(separator)  # Метод строки для разделения по разделителю

    # Находим пересечение списков (общие элементы)
    # Используем преобразование в set (множество) для поиска пересечения
    common_set = set(participants1) & set(participants2)  # Оператор & для пересечения множеств

    # Преобразуем множество обратно в список и сортируем
    common_list = sorted(list(common_set))  # Функция sorted() для сортировки списка

    return common_list

# Списки участников групп (разделитель - вертикальная черта)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
# Вызываем функцию с указанием разделителя "|"
common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator="|"  # Явно указываем разделитель, отличный от запятой
)

print(f"Общие участники: {common_participants}")
print(f"Количество общих участников: {len(common_participants)}")