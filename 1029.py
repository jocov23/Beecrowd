
n = int(input())

fib1 = 2
fib2 = 1
calls = 4


for i in range(0,n):
    
    fib = int(input())
    if fib == 1:
        print (f"fib(1) = 0 calls = 1")
    elif fib == 2:
        print("fib(2) = 2 calls = 1")
    elif fib == 3:
        print("fib(3) = 4 calls = 2")
    else:
        fib1 = 2
        fib2 = 1
        calls, calls1, calls2 = 0,5,3
        for i in range(3,fib):
            result = fib1 + fib2
            calls = calls1 + calls2
            fib2= fib1
            fib1= result
            calls2 = calls1
            calls1= calls +1
            

        print(f"fib({fib}) = {calls} calls = {result}")