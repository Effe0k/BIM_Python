class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        """Геттер для названия (только чтение)"""
        return self._name

    @property
    def author(self):
        """Геттер для автора (только чтение)"""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем сеттер для валидации

    @property
    def pages(self):
        """Геттер для количества страниц"""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Сеттер с валидацией: целое положительное число"""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем сеттер для валидации

    @property
    def duration(self):
        """Геттер для продолжительности"""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Сеттер с валидацией: положительное число с плавающей запятой"""
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self._duration = float(value)
