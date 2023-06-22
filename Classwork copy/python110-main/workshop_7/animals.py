from typing import ClassVar


class Animal:
    objects_created: ClassVar[int] = 0  # static attribute

    def __init__(self, name: str, age: int) -> None:
        Animal.objects_created += 1
        self.name = name
        self.age = age

    @staticmethod
    def give_me_object_count() -> int:
        return Animal.objects_created

    def speak(self) -> str:
        return f'{self.name} - {self.age}: '


class Dog(Animal):
    def speak(self) -> str:
        return f'{super().speak()} woof woof'


class ElectricDog(Dog):

    def __init__(self, name: str, age: int, battery_size: int) -> None:
        super().__init__(name, age)
        self.battery_size = battery_size

    def speak(self) -> str:
        return f'{Animal.speak(self)} zwoof zwoof'


class Cat(Animal):
    def speak(self) -> str:
        return f'{super().speak()} meow meow'


if __name__ == '__main__':
    dog = Dog('doggo', 5)
    dog_1 = ElectricDog('Zdoggo', 1, 4300)
    cat = Cat('catto', 1)

    print(dog.speak())
    print(dog_1.speak())
    print(cat.speak())
    print(Dog.objects_created)
    print(Animal.give_me_object_count())
