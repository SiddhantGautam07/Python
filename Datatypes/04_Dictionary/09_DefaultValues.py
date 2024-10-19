Keys = ["Masala", "Ginger", "Lemon"]
print(Keys)
print()

default_value = "Delicious"
new_dict = dict.fromkeys(Keys, default_value)
print(new_dict)
print()


new_dict = dict.fromkeys(Keys,Keys)
print(new_dict)