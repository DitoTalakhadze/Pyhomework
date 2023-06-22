class Human:
    def __init__(self, name: str, age: int) -> None:
        # initializer / constructor
        self.name = name  # attribute / field
        self.age = age

    def describe_yourself(self) -> None:
        print(f'{self.name} is {self.age} years old')



if __name__ == '__main__':
    human_1 = Human('Givi', 45)  # instance / object
    human_2 = Human('Bill', 67)

    humans: list[Human] = [
        Human('Josh', 26),
        Human('Jane', 44),
        Human('Nick', 31)
    ]

    # print(human_1.name, human_1.age)
    human_1.describe_yourself()
    # print(human_2.name, human_2.age)
    human_2.describe_yourself()



    for human in humans:
        human.describe_yourself()
