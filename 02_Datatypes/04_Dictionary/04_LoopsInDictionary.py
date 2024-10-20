chai_type = {"Masala": "Spicy", "Green": "Mild", "Ginger": "Zesty"}
print(chai_type)
print()

for chai in chai_type:
    print(chai)
print()

for chai in chai_type:
    print(chai,chai_type[chai])
print()

for key,values in chai_type.items():
    print(key,values)
print()
