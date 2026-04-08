n=int(input())

for i in range(n):
    nome = input()
    diff = float(input())
    
    nota = map(float, input().split())
    notas = list(nota)
    
    notas.sort()

    notas.pop(6)
    notas.pop(0)
    notaF = 0
    for x in notas:
        notaF += x

    notaF *= diff

    print(f"{nome} {notaF:.2f}")
