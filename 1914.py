n=int(input())

for x in range(0, n):
    p1, chos1, p2, chos2 = input().split()
    n1, n2 = map(int, input().split())

    resultado = n1+n2
    
    if resultado%2==0:
        if chos1 == "PAR":
            print(p1)
        else:
            print(p2)
    elif resultado%2 != 0:
        if chos1 == "IMPAR":
            print(p1)
        else:
            print(p2)

