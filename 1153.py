
n=int(input())
fat = n
for x in range(n,1,-1):
    fat *= (x - 1)

print(fat)
