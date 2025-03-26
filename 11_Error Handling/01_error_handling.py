file = open('youtube.text','w')

try:
    file.write("chai aur Code")
finally:
    file.close()

with open('youtube.text','w') as file:
    file.write("Chai aru Python")
    