n =int(input())
par=[]
impar=[]

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
        
    else:
        impar.append(num)
        

impar.sort(reverse=True)
par.sort()
for j in par:
    print (j)
for k in impar:
    print(k)