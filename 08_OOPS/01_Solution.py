brand = input("Enter Car Brand Name : ")
model = input("Enter car Model Name : ")
# battery_size = input("Enter Car Battery Size : ")

class Car :
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

my_car = Car(brand,model)
print(my_car.brand)
print(my_car.model)
