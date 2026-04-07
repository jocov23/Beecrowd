n=int(input())
anao = 0
elfo = 0
humano = 0
mago =0
hobbit = 0
for i in range (0, n):
    x,y = input().split()
    if y == "A":
        anao+=1
    elif y == "E":
        elfo+=1
    elif y == "H":
        humano+=1
    elif y == "M":
        mago+=1
    else:
        hobbit+=1
    

print(f"{hobbit} Hobbit(s)")
print(f"{humano} Humano(s)")
print(f"{elfo} Elfo(s)")
print(f"{anao} Anao(oes)")
print(f"{mago} Mago(s)")