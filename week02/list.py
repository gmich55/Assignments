import random
numbers = []
for _ in range(100):
    numbers.append(random.randint(100, 999))

ma = max(numbers)
mi = min(numbers)
av = sum(numbers) / len(numbers)

print("Maximum:", ma)
print("Minimum:", mi)
print("Average:", av)