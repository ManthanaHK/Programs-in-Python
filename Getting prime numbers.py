prime = []
for i in range(1,10):
    remainder = []
    for j in range(2,int(int(i) - 1)):
        remainder.append(i % j)
    if 0 not in remainder:
        prime.append(i)
print(prime)
