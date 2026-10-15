n = int(input("Enter the height of the tree: "))

if n % 2 == 0:
    n += 1  

h = (n + 1) // 2
for i in range(h):
    space = " " * (h - i - 1)
    stars = "*" * (2 * i + 1)
    print(space + stars)    