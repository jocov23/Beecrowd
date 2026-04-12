op = input()
soma, cont=0,0
for i in range (12):
    for j in range(12):
        num = float(input())

        if j > 0 + i:
            soma += num
            cont+=1

if op == "S":
    print(f"{soma:.1f}")
else:
    print(f"{soma/cont:.1f}")

    