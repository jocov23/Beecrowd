n =int(input())

for i in range(n):
    qnt = int(input())
    
    
    lista = map(int,input().split())
    lista1=list(lista)
    igual=0
    lista2= []
    for x in lista1:
        lista2.append(x)

    lista1.sort(reverse=True)
    tam = len(lista1)
    
    for i in range(tam):
        elemento1 = lista1.pop()
        elemento2 = lista2.pop()
        
        if elemento1 == elemento2:

            igual +=1


    print(igual)
    
    