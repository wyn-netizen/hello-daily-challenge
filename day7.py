total = 0
for i in range (1,101):
    total += i
    print(total)

for i in range(1,11):
    print(f"{i}的平方是{i**2}")

n = 10
while n >= 1:
    print(n)
    n -= 1

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="  ")
    print()
                                                                                     