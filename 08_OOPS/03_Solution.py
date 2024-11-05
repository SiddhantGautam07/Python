brand = input("Enter Car brand Name : ")
model = input("Enter Car Model name : ")
batter_size = input("Enter Car Battery_Size : ")

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar (Car):
    def __init__(self, brand, model,Battery_size):
        super().__init__(brand, model)
        self.battery_size = batter_size

my_car = ElectricCar(brand,model,batter_size)
print("Brand Name of Your Car :",my_car.brand)
print("Model Name of your car :",my_car.model)
print("Full name of Your Car :",my_car.full_name())
print("Battery Size of Car :",my_car.battery_size)
