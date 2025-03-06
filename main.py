# Импорт необходимых модулей
from enum import Enum  # Импорт модуля Enum для создания перечислимых типов


# Определение перечислимого типа для цвета
class Color(Enum):
    # Перечисление цветов с присвоением им числовых значений
    RED = 0
    ORANGE = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    PURPLE = 5


# Абстрактный базовый класс "Фигура"
class Figure:
    # Конструктор базового класса для инициализации общих параметров фигуры
    def __init__(self, color, lastEditDate):
        # Общие параметры для всех фигур: цвет и дата последнего редактирования
        self.color = color
        self.lastEditDate = lastEditDate

    # Виртуальный метод для печати информации о фигуре
    def print(self):
        # Выбрасывает исключение, если метод не реализован в дочернем классе
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")


# Класс для круга
class Circle(Figure):
    # Конструктор класса Circle для инициализации параметров круга
    def __init__(self, centerX, centerY, radius, color, lastEditDate):
        # Вызов конструктора базового класса для инициализации общих параметров
        super().__init__(color, lastEditDate)
        # Уникальные параметры для круга: координаты центра и радиус
        self.centerX = centerX
        self.centerY = centerY
        self.radius = radius

    # Реализация метода для печати информации о круге
    def print(self):
        # Вывод информации о круге на экран
        print(
            f"Круг: ({self.centerX}, {self.centerY}), "
            f"радиус = {self.radius}, "
            f"цвет = {self.color.name}, "
            f"дата редактирования = {self.lastEditDate}")


# Класс для прямоугольника
class Rectangle(Figure):
    # Конструктор класса Rectangle для инициализации параметров прямоугольника
    def __init__(self, x1, y1, x2, y2, color, lastEditDate):
        # Вызов конструктора базового класса для инициализации общих параметров
        super().__init__(color, lastEditDate)
        # Уникальные параметры для прямоугольника: координаты левого верхнего и правого нижнего углов
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    # Реализация метода для печати информации о прямоугольнике
    def print(self):
        # Вывод информации о прямоугольнике на экран
        print(
            f"Прямоугольник: ({self.x1}, {self.y1}) - "
            f"({self.x2}, {self.y2}), "
            f"цвет = {self.color.name}, "
            f"дата редактирования = {self.lastEditDate}")


# Класс для треугольника
class Triangle(Figure):
    # Конструктор класса Triangle для инициализации параметров треугольника
    def __init__(self, x1, y1, x2, y2, x3, y3, color, lastEditDate):
        # Вызов конструктора базового класса для инициализации общих параметров
        super().__init__(color, lastEditDate)
        # Уникальные параметры для треугольника: координаты трёх вершин
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    # Реализация метода для печати информации о треугольнике
    def print(self):
        # Вывод информации о треугольнике на экран
        print(
            f"Треугольник: ({self.x1}, {self.y1}) ({self.x2}, {self.y2}) "
            f"({self.x3}, {self.y3}), "
            f"цвет = {self.color.name}, "
            f"дата редактирования = {self.lastEditDate}")


# Контейнер для хранения фигур
class FigureContainer:
    # Конструктор контейнера для инициализации пустого списка фигур
    def __init__(self):
        # Используется список для хранения объектов фигур
        self.figures = []

    # Метод для добавления фигуры в контейнер
    def addFigure(self, figure):
        # Добавление фигуры в конец списка
        self.figures.append(figure)

    # Метод для удаления фигур по заданному условию
    def removeFigures(self, condition):
        # Словарь для сопоставления названий цветов с их перечислениями
        color_map = {
            "red": Color.RED,
            "orange": Color.ORANGE,
            "yellow": Color.YELLOW,
            "green": Color.GREEN,
            "blue": Color.BLUE,
            "purple": Color.PURPLE
        }

        # Удаление фигур по заданному цвету
        if condition in color_map:
            self.figures = [f for f in self.figures if f.color != color_map[condition]]

    # Метод для печати содержимого контейнера
    def printContainer(self):
        # Вывод информации о всех фигурах в контейнере
        for figure in self.figures:
            figure.print()


# Функция для чтения файла и парсинга команд
def readFile(filename):
    # Создание пустого контейнера для фигур
    container = FigureContainer()

    # Открытие файла для чтения
    with open(filename, 'r') as file:
        # Чтение файла построчно
        for line in file:
            # Удаление пробельных символов в начале и конце строки
            line = line.strip()

            # Проверка типа команды
            if line.startswith("ADD"):
                # Парсинг данных для команды ADD
                parts = line.split()
                figureType = parts[1]

                try:
                    # Создание объекта фигуры на основе типа
                    if figureType == "Circle":
                        # Создание круга
                        centerX, centerY, radius = map(int, parts[2:5])
                        color = Color[parts[5].upper()]
                        lastEditDate = parts[6]
                        figure = Circle(centerX, centerY, radius, color, lastEditDate)
                    elif figureType == "Rectangle":
                        # Создание прямоугольника
                        x1, y1, x2, y2 = map(float, parts[2:6])
                        color = Color[parts[6].upper()]
                        lastEditDate = parts[7]
                        figure = Rectangle(x1, y1, x2, y2, color, lastEditDate)
                    elif figureType == "Triangle":
                        # Создание треугольника
                        x1, y1, x2, y2, x3, y3 = map(float, parts[2:8])
                        color = Color[parts[8].upper()]
                        lastEditDate = parts[9]
                        figure = Triangle(x1, y1, x2, y2, x3, y3, color, lastEditDate)
                    else:
                        # Обработка ошибки: неподдерживаемый тип фигуры
                        print(f"Неподдерживаемый тип фигуры: {figureType}")
                        continue

                    # Добавление фигуры в контейнер
                    container.addFigure(figure)
                except (IndexError, ValueError, KeyError):
                    # Обработка ошибки: неправильные данные для создания фигуры
                    print(f"Неправильные данные для создания фигуры: {line}")

            elif line.startswith("REM"):
                # Парсинг условия для команды REM
                condition = line.split()[1]
                # Удаление фигур по условию
                container.removeFigures(condition)

            elif line == "PRINT":
                # Печать содержимого контейнера
                container.printContainer()


# Пример использования
if __name__ == "__main__":
    # Вызов функции для чтения файла и обработки команд
    readFile("commands.txt")