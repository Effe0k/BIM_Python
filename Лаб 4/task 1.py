from typing import Optional, Union

class ConiferousTree:
    """
    Базовый класс для хвойных деревьев.

    Представляет общие характеристики и поведение всех хвойных деревьев.
    """

    def __init__(self, species: str, height: float, age: int) -> None:
        """
        Конструктор базового класса.

        Args:
            species: Название вида дерева
            height: Высота дерева в метрах
            age: Возраст дерева в годах
        """
        self.species = species
        self.height = height
        self.age = age
        self._needle_type = "игольчатая"  # непубличный атрибут - тип хвои
        self._is_evergreen = True  # непубличный атрибут - вечнозеленое

    def grow(self, years: int) -> None:
        """
        Метод роста дерева.

        Args:
            years: Количество лет роста

        Note:
            Метод инкапсулирует логику роста, так как разные виды
            хвойных деревьев растут с разной скоростью.
        """
        for _ in range(years):
            self.age += 1
            # Базовая логика роста - 0.3 метра в год
            self.height += 0.3

    def get_info(self) -> str:
        """
        Получить информацию о дереве.

        Returns:
            Строка с основной информацией о дереве
        """
        return (f"{self.species}: высота {self.height} м, "
                f"возраст {self.age} лет, хвоя {self._needle_type}")

    def __str__(self) -> str:
        """
        Пользовательское строковое представление дерева.

        Returns:
            Читаемая строка с информацией о дереве
        """
        return f"{self.species} (высота: {self.height}м, возраст: {self.age} лет)"

    def __repr__(self) -> str:
        """
        Техническое строковое представление для отладки.

        Returns:
            Строка, позволяющая воссоздать объект
        """
        return f"{self.__class__.__name__}(species='{self.species}', height={self.height}, age={self.age})"


class Spruce(ConiferousTree):
    """
    Класс Ель, наследующий базовый класс ConiferousTree.

    Представляет особенности ели как вида хвойных деревьев.
    """

    def __init__(self, height: float, age: int, cone_length: float) -> None:
        """
        Конструктор дочернего класса.

        Args:
            height: Высота ели в метрах
            age: Возраст ели в годах
            cone_length: Длина шишек в сантиметрах
        """
        # Расширяем конструктор базового класса
        super().__init__(species="Ель обыкновенная", height=height, age=age)
        self.cone_length = cone_length
        self._needle_type = "короткая игольчатая"  # переопределяем непубличный атрибут
        self._branch_density = "густая"  # дополнительный непубличный атрибут

    def grow(self, years: int) -> None:
        """
        Перегруженный метод роста для ели.

        Причина перегрузки: ели в молодом возрасте растут быстрее,
        чем в зрелом, что отличает их от базовой модели равномерного роста.

        Args:
            years: Количество лет роста
        """
        for _ in range(years):
            self.age += 1
            # Ель растет быстрее в молодом возрасте (до 20 лет)
            if self.age <= 20:
                self.height += 0.5
            else:
                self.height += 0.2

    def produce_resin(self) -> str:
        """
        Дополнительный метод для ели - выделение смолы.

        Returns:
            Сообщение о выделении смолы
        """
        return "Ель выделяет смолу для защиты от вредителей"

    def __str__(self) -> str:
        """
        Перегруженный пользовательский метод строкового представления.

        Returns:
            Расширенная информация о ели
        """
        return (f"{self.species} (высота: {self.height}м, возраст: {self.age} лет, "
                f"длина шишек: {self.cone_length}см)")

    def __repr__(self) -> str:
        """
        Перегруженный технический метод строкового представления.

        Returns:
            Строка, позволяющая воссоздать объект ели
        """
        return (f"{self.__class__.__name__}(height={self.height}, age={self.age}, "
                f"cone_length={self.cone_length})")


class Pine(ConiferousTree):
    """
    Класс Сосна, наследующий базовый класс ConiferousTree.

    Представляет особенности сосны как вида хвойных деревьев.
    """

    def __init__(self, height: float, age: int, needle_length: float) -> None:
        """
        Конструктор дочернего класса.

        Args:
            height: Высота сосны в метрах
            age: Возраст сосны в годах
            needle_length: Длина хвои в сантиметрах
        """
        # Расширяем конструктор базового класса
        super().__init__(species="Сосна обыкновенная", height=height, age=age)
        self.needle_length = needle_length
        self._needle_type = "длинная игольчатая"  # переопределяем непубличный атрибут
        self._root_system = "стержневая"  # дополнительный непубличный атрибут

    def grow(self, years: int) -> None:
        """
        Перегруженный метод роста для сосны.

        Причина перегрузки: сосны имеют более медленный темп роста
        по сравнению с елями, но живут дольше и достигают большей высоты.

        Args:
            years: Количество лет роста
        """
        for _ in range(years):
            self.age += 1
            # Сосна растет равномерно, но медленнее ели
            self.height += 0.25

    def produce_pollen(self) -> str:
        """
        Дополнительный метод для сосны - образование пыльцы.

        Returns:
            Сообщение о пылении
        """
        return "Сосна выделяет пыльцу в период цветения"

    def __str__(self) -> str:
        """
        Перегруженный пользовательский метод строкового представления.

        Returns:
            Расширенная информация о сосне
        """
        return (f"{self.species} (высота: {self.height}м, возраст: {self.age} лет, "
                f"длина хвои: {self.needle_length}см)")

    def __repr__(self) -> str:
        """
        Перегруженный технический метод строкового представления.

        Returns:
            Строка, позволяющая воссоздать объект сосны
        """
        return (f"{self.__class__.__name__}(height={self.height}, age={self.age}, "
                f"needle_length={self.needle_length})")


if __name__ == "__main__":
    # Пример использования классов
    spruce = Spruce(height=5.2, age=15, cone_length=8.5)
    pine = Pine(height=4.8, age=12, needle_length=6.0)

    print("=== Ель ===")
    print(spruce)
    print(f"Представление: {repr(spruce)}")
    print(spruce.get_info())
    print(f"Рост за 3 года:")
    spruce.grow(3)
    print(spruce)
    print(spruce.produce_resin())

    print("\n=== Сосна ===")
    print(pine)
    print(f"Представление: {repr(pine)}")
    print(pine.get_info())
    print(f"Рост за 3 года:")
    pine.grow(3)
    print(pine)
    print(pine.produce_pollen())