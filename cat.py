import names  # type: ignore
import random
from typing import Union

class Cat:
    def __init__(self, name: str, breed: str, color: str, age: Union[int, float], weight: Union[int, float], category: str) -> None:
        self.name = name
        self.breed = breed
        self.color = color
        if isinstance(age, (int, float)):
            self.age = round(float(age), 1)
        else:
            raise ValueError("Age must be a number")
        if isinstance(weight, (int, float)):
            self.weight = round(float(weight), 1)
        else:
            raise ValueError("Weight must be a number")
        self.category = category

    def get_info(self) -> str:
        return f"Cat({self.name}, {self.breed}) - {self.color}, {self.age} years old, {self.weight} kg, {self.category}"

    def get_message(self) -> str:
        if self.age < 0.5:
            age_category = "Кошеня"
        elif self.age < 2:
            age_category = "Підліток"
        elif self.age < 10:
            age_category = "Доросла"
        elif self.age < 14:
            age_category = "Літка"
        else:
            age_category = "Дуже літня"
        
        return f'"{age_category} {self.name} породи {self.breed}, що відноситься до {self.category} пород", ' \
               f'"{self.age} years old and weighs {self.weight} kg, has {self.color} color"'

    def __repr__(self) -> str:
        return f"Cat({self.name}, {self.breed}, {self.color}, {self.age}, {self.weight}, {self.category})"

class Generator:
    breeds = ["Персидська", "Сіамська", "Британська", "Мейн-кун", "Русская голубая", "Шотландська"]
    colors = ["білий", "чорний", "сірий", "різнобарвний", "коричневий"]
    categories = ["короткошерстий", "довгошерстий"]

    @staticmethod
    def generate_single() -> "Cat":
        """Метод автоматичного створення екземпляру класу Cat з
        випадковими значеннями кожної властивості класу
        """
        name = names.get_first_name()
        breed = random.choice(Generator.breeds)
        color = random.choice(Generator.colors)
        age = round(random.uniform(0.1, 20), 1)  # Вік від 0.1 до 20 років (включно), округлення до десятих
        weight = round(random.uniform(0.5, 10), 1)  # Вага від 0.5 до 10 кг (включно), округлення до десятих
        category = random.choice(Generator.categories)

        return Cat(name, breed, color, age, weight, category)

    def generate_1000(self) -> list:
        """Метод генерування 1000 об'єктів класу Student"""
        plist = list()
        for i in range(1000):
            plist.append(self.generate_single())
        return plist

    def generate_10_000(self) -> list:
        """Метод генерування 10 000 об'єктів класу Student"""
        plist = [self.generate_single() for i in range(10000)]
        return plist

gen = Generator()

Cat_1000 = gen.generate_1000()

for caty in Cat_1000[:5]:
    print(caty)

cat_10000 = gen.generate_10_000()

for catys in cat_10000[:5]:
    print(catys)
cat1 = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
cat2 = Cat("Мурзик", "Сіамська", "сіра", 3, 4, "короткошерстий")
print(cat1)
print(cat1.get_info())
print(cat1.get_message())

print(cat2.get_info())
print(cat2.get_message())