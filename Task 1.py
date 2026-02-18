# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Tree:

    """
    Класс, описывающий дерево.
    Дерево характеризуется породой, возрастом и высотой.
    """

    def __init__(self, species: str, age_years: [int, float], height_meters: [int, float]):
        if not isinstance(species, str):
            raise TypeError("Должен быть введен строковый тип данных для породы")
        if age_years <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        if height_meters <= 0:
            raise ValueError("Высота должна быть положительным числом")

        self.species = species
        self.age_years = age_years
        self.height_meters = height_meters

    """
    Метод увеличивает возраст дерева и имитирует рост.
    Вводится количество лет years для роста
    """

    def grow(self, years: [int, float]) -> None:
        if years <= 0:
            raise ValueError("Количество лет для роста должно быть положительным")
        ...

    """
    Метод возвращает строку с описанием дерева.
    Возвращает строку с описанием дерева
    """
    def get_info(self) -> str:
        ...

class FacebookUser:

    """
    Класс, описывающий пользователя Facebook.
    Пользователь имеет имя, email.
    """

    def __init__(self, username: str, email: str):
        if not isinstance(username, str):
            raise TypeError("Должен быть введен строковый тип данных для имени пользователя")
        if not (3 <= len(username) <= 30) or not username.isalnum():
            raise ValueError("Имя пользователя должно быть длиной 3-30 символов и содержать только буквы и цифры")
        if not isinstance(email, str):
            raise TypeError("Должен быть введен строковый тип данных для email")
        if "@" not in email:
            raise ValueError("Некорректный email адрес")

        self.username = username
        self.email = email

    """
    Метод добавляет друга в список друзей.
    Вводится объект пользователя FacebookUser, которого добавляем в друзья. True, если друг добавлен успешно.
    """

    def add_friend(self, friend_user: 'FacebookUser') -> bool:
        ...

class Smartphone:

    """
    Класс, описывающий смартфон.
    Смартфон имеет модель, уровень заряда и состояние блокировки.
    """

    def __init__(self, model: str, battery_percentage: [int, float]):
        if not isinstance(model, str):
            raise TypeError("Должен быть введен строковый тип данных для модели")
        if not (0 <= battery_percentage <= 100):
            raise ValueError("Уровень заряда должен быть от 0 до 100")

        self.model = model
        self.battery = battery_percentage
        
    """
    Метод заряжает телефон.
    Вводится время зарядки в минутах minutes
    """

    def charge(self, minutes: [int, float]) -> int:
        if minutes <= 0:
            raise ValueError("Время зарядки должно быть положительным")
        ...

    """
    Метод разблокирует телефон по паролю.
    Вводится пароль password для разблокировки. True, если разблокировка успешна, иначе False.
    """

    def unlock(self, password: str) -> bool:
        ...

if __name__ == "__main__":
    doctest.testmod()# TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

#По итогу создал идеи и заглушки под методы не расписывая их
