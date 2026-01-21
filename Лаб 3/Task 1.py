# TODO Напишите функцию для поиска индекса товара

def find_item_index(items, target):
    # Проверяем, есть ли искомый товар в списке
    if target in items:
        # Используем метод списка index() для поиска индекса
        return items.index(target)
    else:
        # Возвращаем None, если товар не найден
        return None

# Список товаров для поиска
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Ищем несколько товаров в цикле
for find_item in ['банан', 'груша', 'персик']:
    # TODO Вызовите функцию, что получить индекс товара
    index_item = find_item_index(items_list, find_item)  # Вызов функции поиска индекса
    # Проверяем результат поиска
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")