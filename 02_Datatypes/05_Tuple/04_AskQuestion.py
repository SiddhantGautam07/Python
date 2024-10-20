tea = ("Masala","Green","Lemon")
print(tea)
print()

more_tea = ("Harbal", "Earl Grey")
print(more_tea)
print()

all_tea = tea + more_tea
print(all_tea)
print()

if "Green" in all_tea:
    print("I have Green tea")
print()

more_tea = ("Harbal","Earl Grey","Harbal")
print(more_tea)
print()

more_tea.count("Harbal")
print(more_tea)
print()

more_tea.count("Herb")
print(more_tea)
print()

print(type(more_tea))
