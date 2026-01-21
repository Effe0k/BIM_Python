# TODO  Напишите функцию count_letters
def count_letters(text):

    letter_counts = {}

    # Проходим по каждому символу в тексте
    for char in text:
        # Проверяем, является ли символ буквой
        if char.isalpha():
            # Приводим к нижнему регистру для учета без учета регистра
            char_lower = char.lower()

            # Увеличиваем счетчик для этой буквы
            if char_lower in letter_counts:
                letter_counts[char_lower] += 1
            else:
                letter_counts[char_lower] = 1

    return letter_counts

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_counts):
    # Подсчитываем общее количество букв
    total_letters = sum(letter_counts.values())

    # Если текст пустой, возвращаем пустой словарь
    if total_letters == 0:
        return {}

    # Создаем словарь для частот
    frequencies = {}

    # Рассчитываем частоту для каждой буквы
    for letter, count in letter_counts.items():
        # Вычисляем частоту
        frequency = count / total_letters

        # Округляем до 2 знаков после запятой
        rounded_frequency = round(frequency, 2)

        # Сохраняем результат
        frequencies[letter] = rounded_frequency

    return frequencies
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# Шаг 1: Подсчитываем количество каждой буквы
letters_count_dict = count_letters(main_str)

# Шаг 2: Вычисляем частоту каждой буквы
frequency_dict = calculate_frequency(letters_count_dict)

# Шаг 3: Распечатываем результат в столбик
for letter, frequency in frequency_dict.items():
    print(f"{letter}: {frequency}")