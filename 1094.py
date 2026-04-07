n=int(input())
rato = 0
sapo = 0
coelho = 0
for i in range (0, n):
    x,y = input().split()
    x=int(x)
    if y == "R":
        rato+=x
    elif y == "S":
        sapo+=x
    else:
        coelho+=x

total = rato+sapo+coelho
percR= float((rato * (100/total)))
percS=float((sapo * (100/total)))
percC=float((coelho* (100/total)))

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {percC:.2f} %")
print(f"Percentual de ratos: {percR:.2f} %")
print(f"Percentual de sapos: {percS:.2f} %")    
    