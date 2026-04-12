n = int(input())

for i in range(n):
    areia = input()
    lado1=[]
    lado2=[]
    diamantes = 0
    for char in areia:
        if char == "<":
            lado1.append(char)
        elif char == ">":
            if len(lado1) == 0:
                pass
            else:
                lado1.pop()
                diamantes += 1
    print(diamantes)

   
 

