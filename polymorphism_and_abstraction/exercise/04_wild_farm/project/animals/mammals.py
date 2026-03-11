from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat



class Mouse(Mammal):
    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    @property
    def weight_increment(self) -> float:
        return 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    @property
    def allowed_food(self):
        return [Vegetable, Meat]

    @property
    def weight_increment(self) -> float:
        return 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"