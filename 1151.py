


seq = [0, 1, 1]
fib = int(input())
if fib == 1:
    print ("0")
elif fib == 2:
    print("0 1")
elif fib == 3:
    print("0 1 1")
else:
    fib1 = 2
    fib2 = 1
    
    for i in range(3,fib):
        result = fib1 + fib2
        fib2= fib1
        fib1= result
        seq.append(fib2)
    for x in seq:
        if x == seq[-1]:
            print(x)
        else:
            print(x, end=" ")
    

        
        
