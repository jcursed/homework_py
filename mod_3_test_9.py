class Car:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name

car = Car("nissan", "note")

print(f'Brand is {car.brand} and name is {car.name}')