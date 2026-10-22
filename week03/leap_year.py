y = int(input("give year: "))

if y % 400 == 0:
    print(F"{y} is a leap year")
elif y % 100 == 0:
    print(F"{y} is not a leap year")
elif y % 4 == 0:
    print(F"{y} is a leap year")
else:
    print(F"{y} is not a leap year")
