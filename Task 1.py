# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Tree:
    """
    Класс, описывающий дерево.
    Дерево характеризуется породой, возрастом и высотой.

    Примеры:
        oak = Tree("Дуб", 10, 5.5)
        oak.get_info()  # 'Дерево: Дуб, возраст: 10 лет, высота: 5.5 м'
        oak.grow(5)
        oak.get_info()  # 'Дерево: Дуб, возраст: 15 лет, высота: 6.0 м'
        oak.grow(-1)  # ValueError: Количество лет для роста должно быть положительным
    """

    def __init__(self, species: str, age_years, height_meters):
        """
        Инициализация дерева.

        Args:
            species: Порода дерева (строка)
            age_years: Возраст дерева в годах (положительное число)
            height_meters: Высота дерева в метрах (положительное число)

        Raises:
            TypeError: Если species не является строкой
            ValueError: Если age_years или height_meters не положительные
        """
        if not isinstance(species, str):
            raise TypeError("Должен быть введен строковый тип данных для породы")
        if not isinstance(age_years, (int, float)) or age_years <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        if not isinstance(height_meters, (int, float)) or height_meters <= 0:
            raise ValueError("Высота должна быть положительным числом")

        self.species = species
        self.age_years = age_years
        self.height_meters = height_meters

    def grow(self, years):
        """
        Метод увеличивает возраст дерева и имитирует рост.

        Args:
            years: Количество лет для роста (положительное число)

        Raises:
            ValueError: Если years <= 0
        """
        if not isinstance(years, (int, float)) or years <= 0:
            raise ValueError("Количество лет для роста должно быть положительным числом")

        self.age_years += years
        # Имитация роста: дерево растет примерно на 0.1 м в год
        self.height_meters += years * 0.1

    def get_info(self) -> str:
        """
        Возвращает строку с описанием дерева.

        Returns:
            Строка с описанием дерева
        """
        return f"Дерево: {self.species}, возраст: {self.age_years} лет, высота: {self.height_meters} м"


class FacebookUser:
    """
    Класс, описывающий пользователя Facebook.
    Пользователь имеет имя, email и список друзей.

    Примеры:
        user1 = FacebookUser("john_doe", "john@example.com")
        user2 = FacebookUser("jane_smith", "jane@example.com")
        user1.add_friend(user2)  # True
        user1.get_friends_count()  # 1
        user3 = FacebookUser("ab", "invalid_email")  # ValueError: Имя пользователя должно быть длиной 3-30 символов и содержать только буквы и цифры
    """

    def __init__(self, username: str, email: str):
        """
        Инициализация пользователя Facebook.

        Args:
            username: Имя пользователя (строка, 3-30 символов, буквы и цифры)
            email: Email адрес (строка, должен содержать @)

        Raises:
            TypeError: Если username или email не являются строками
            ValueError: Если username не соответствует требованиям или email некорректный
        """
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
        self.friends = []

    def add_friend(self, friend_user):
        """
        Метод добавляет друга в список друзей.

        Args:
            friend_user: Объект пользователя Facebook, которого добавляем в друзья

        Returns:
            True, если друг добавлен успешно, False если друг уже в списке

        Raises:
            TypeError: Если friend_user не является экземпляром FacebookUser
        """
        if not isinstance(friend_user, FacebookUser):
            raise TypeError("Друг должен быть экземпляром класса FacebookUser")

        if friend_user in self.friends:
            return False

        self.friends.append(friend_user)
        return True

    def get_friends_count(self) -> int:
        """
        Возвращает количество друзей пользователя.

        Returns:
            Количество друзей
        """
        return len(self.friends)


class Smartphone:
    """
    Класс, описывающий смартфон.
    Смартфон имеет модель, уровень заряда и состояние блокировки.

    Примеры:
        phone = Smartphone("iPhone 13", 50)
        phone.charge(30)  # 80
        phone.unlock("1234")  # False
        phone.set_password("1234")
        phone.unlock("1234")  # True
        phone.charge(-10)  # ValueError: Время зарядки должно быть положительным
    """

    def __init__(self, model: str, battery_percentage):
        """
        Инициализация смартфона.

        Args:
            model: Модель смартфона (строка)
            battery_percentage: Уровень заряда (число от 0 до 100)

        Raises:
            TypeError: Если model не является строкой
            ValueError: Если battery_percentage вне диапазона 0-100
        """
        if not isinstance(model, str):
            raise TypeError("Должен быть введен строковый тип данных для модели")
        if not isinstance(battery_percentage, (int, float)) or not (0 <= battery_percentage <= 100):
            raise ValueError("Уровень заряда должен быть от 0 до 100")

        self.model = model
        self.battery = battery_percentage
        self.is_locked = True
        self.password = None

    def charge(self, minutes: int) -> int:
        """
        Метод заряжает телефон.

        Args:
            minutes: Время зарядки в минутах (положительное целое число)

        Returns:
            Новый уровень заряда после зарядки

        Raises:
            ValueError: Если minutes <= 0
        """
        if not isinstance(minutes, (int, float)) or minutes <= 0:
            raise ValueError("Время зарядки должно быть положительным")

        # Зарядка: 1 минута = 1% заряда
        self.battery = min(100, self.battery + minutes)
        return self.battery

    def set_password(self, password: str) -> None:
        """
        Устанавливает пароль для разблокировки телефона.

        Args:
            password: Пароль для разблокировки (строка)
        """
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")

        self.password = password

    def unlock(self, password: str) -> bool:
        """
        Метод разблокирует телефон по паролю.

        Args:
            password: Пароль для разблокировки

        Returns:
            True, если разблокировка успешна, иначе False
        """
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")

        if self.password is None:
            # Если пароль не установлен, телефон всегда разблокируется
            self.is_locked = False
            return True

        if password == self.password:
            self.is_locked = False
            return True

        return False


if __name__ == "__main__":
    doctest.testmod()# TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
