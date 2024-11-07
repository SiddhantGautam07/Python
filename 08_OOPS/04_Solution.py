class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


new_car = ElectricCar("Toyoto", "Corolla", "100kwh")
# print(new_car.__brand)
print(new_car.get_brand())



# print(new_car.model)
# print(new_car.full_name())
# print(new_car.battery_size)

