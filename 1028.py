n = int(input())

for i in range(0,n):
    n1, n2 = map(int, input().split())
    div = 2
    pilha = 1
    resto = n1%n2

    while resto != 0:
        n1 = n2
        n2 = resto
        resto = n1%n2
        
        
    
    print(n2)