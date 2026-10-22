import random

n = []

for i in range (20):
    n.append(random.randint(1, 100))
    print (n)

for i in range (len(n)-1):
    for j in range (len(n)-1-i):
        if n[j] > n[j+1]:
            t = n[j]
            n[j] = n[j+1]
            n[j+1] = t

print ("Sorted list: ", n)            