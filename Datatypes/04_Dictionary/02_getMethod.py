chai_type = {"masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_type)
print()

# Accessing 

print(chai_type["Ginger"])
print()

# print(chai_type["Masala"])        It gives error if key is incorrect
print()

# Accessing by get Method()

print(chai_type.get("masala"))
print()

print(chai_type.get("Masala"))      # It returns none if key is incorrect
print()

