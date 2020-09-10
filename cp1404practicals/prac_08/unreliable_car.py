from car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliablity = reliability

    def drive(self, distance):
        random_int = randint(1, 100)
        print(random_int)
        if random_int >= self.reliablity:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven




