chai_type = {"Masala": "Spicy", "Green": "Mild", "Ginger": "Zesty", "Black": "Strong"}
print(chai_type)
print()

chai_type.pop("Ginger")
print(chai_type)
print()

chai_type.popitem()
print(chai_type)
print()

del chai_type ["Green"]
print(chai_type)
print()

