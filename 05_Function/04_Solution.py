import math

radius = int(input("Enter the radius : "))

def circle_stats(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return area, circumference
    # print("Hello World")
    # print("Siddhant Gautam")      // It is not executes after return keywords is used.

c,a = circle_stats(radius)

print("Circumference : ",c, "Area : ",a)


