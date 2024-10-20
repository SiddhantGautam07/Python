pet_species = input("Enter Your Pet Species : ")
pet_age = int(input("Enter your Pet Age : "))

food = "Puppy Food" if pet_age <= 2 else "Senior Cat Food"

if pet_species == "Dog" :
    food = "Puppy Food"
elif pet_species == "Cat":
    food = "Senior Cat Food"
else:
    food = "None"

print(food)
