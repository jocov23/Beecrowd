n = int(input())
maior=n
pos=1

for x in range(2,101):
    n = int(input())
    if n > maior:
        maior = n
        pos = x
    

print(maior)
print(pos)
