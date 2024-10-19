Score =100

if Score >= 101:
    print("Please Verify Your Grade again")
    exit()

if Score >= 90:
    grade = "A"
elif Score >= 80:
    grade = "B"
elif Score >= 70:
    grade = "C"
elif Score >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade :",grade)
