class Car:

    total_car = 0

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    
    def full_name(self):
        return f"{self.brand} {self.model}"

    @staticmethod
    def general_description():
        return "Car is a means of Transportation"

class ElctricCar (Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

tesla = ElctricCar("Tesla", "Model S", "100Kwh")
# print(tesla.brand)

# safari = Car("Tata","Safari")
# print(safari.general_description())
# print(Car.general_description())

# new_car = Car("Tata","Nexon")

print(isinstance(tesla,Car))
print(isinstance(tesla,ElctricCar))


