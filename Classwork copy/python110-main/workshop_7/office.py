import random

from intro_oop import Human


class Office:
    def __init__(self, size: int) -> None:
        self.size = size
        self.employees: list[Human] = []

    def is_full(self) -> bool:
        return self.size <= len(self.employees)

    def info(self) -> str:
        employees_string: str = ', '.join(
            [
                employee.name
                for employee in self.employees
            ]
        )

        return f'{len(self.employees)}/{self.size}: {employees_string}'


class Company:
    def __init__(self, name: str, capital: int = 100_000) -> None:
        self.name = name
        self.capital = capital
        self.offices: list[Office] = []  # composition

    def build_new_office(self, size: int = 10) -> None:
        self.offices.append(Office(size))

    def find_free_office(self) -> Office | None:
        for office in self.offices:
            if not office.is_full():
                return office

    def recruit_employee(self, employee: Human) -> None:
        """
        იპოვეთ თავისუფალი ადგილი ნებისმიერ ოფისში
        თუ ვერ იპოვეთ ამოაგდეთ ერორი
        """
        available_office: Office | None = self.find_free_office()
        if available_office:
            available_office.employees.append(employee)
        else:
            raise Exception('Company has no room available in any office')


def main() -> None:
    comp = Company("Microsoft")
    humans: list[Human] = [
        Human(f"Name {i}", random.randint(0, 45))
        for i in range(100)
    ]

    comp.build_new_office(10)

    for human in humans[:10]:
        comp.recruit_employee(human)

    comp.build_new_office(5)
    comp.recruit_employee(humans[10])
    print(comp.offices[0].info())
    print(comp.offices[1].info())


if __name__ == '__main__':
    main()