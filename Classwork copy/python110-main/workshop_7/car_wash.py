import time
start_time: float = time.time()


class Car:
    def __init__(self, brand: str, year: int) -> None:
        self.brand = brand
        self.year = year


class CarWash:
    def __init__(self, spaces: int, wash_time: int = 2) -> None:
        self.spaces = spaces
        self.cars_in_progress: dict[Car, float] = {}
        self.wash_time: int = wash_time

    def check_washed_cars(self) -> None:
        for _car, _start_time in self.cars_in_progress.copy().items():
            time_elapsed: float = time.time() - _start_time
            car_has_been_washed: bool = time_elapsed >= self.wash_time
            if car_has_been_washed:
                self.cars_in_progress.pop(_car)

    def wash_car(self, car: Car) -> None:
        self.check_washed_cars()
        if self.spaces == len(self.cars_in_progress):
            raise Exception('We are full')
        self.cars_in_progress[car] = time.time()
        print(f'Started washing {car.brand} - {car.year}')


my_cars: list[Car] = [
    Car('Tesla', 2016),
    Car('Mercedes', 2019),
    Car('Lexus', 2019)
]

nearest_car_wash: CarWash = CarWash(1)

nearest_car_wash.wash_car(my_cars[1])
time.sleep(2)
nearest_car_wash.wash_car(my_cars[2])
time.sleep(2)
nearest_car_wash.wash_car(my_cars[0])

print(time.time() - start_time)

