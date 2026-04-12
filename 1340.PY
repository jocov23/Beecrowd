while True:
    try:
        n = int(input())
        items=[]
        items2=[]
        priorq = 0
        stack = 0
        queue = 0
        invalido = 0
        for x in range(n):
            com, item = map(int, input().split())
            if com == 1:
                items.append(item)
                items2.append(item)
                items2.sort(reverse=True)
            if com == 2:
                if item in items and item in items2:
                    pass
                else:
                    invalido = 1
                if item == items2[0]:
                    items2.pop(0)
                else:
                    priorq = 1
                if item == items[-1]:
                    items.pop()
                else:
                    stack = 1
                if len(items) == 0:
                    pass
                else:
                    if item == items[0]:
                        items.pop(0)
                    else:
                        queue = 1
                
                
                

                
        
        
        if stack==1 and queue== 1 and priorq ==0:
            print("priority queue")
        elif stack==0 and priorq == 1 and queue == 1:
            print("stack")
        elif queue== 0 and stack ==1 and priorq ==1:
            print("queue")
        elif queue ==1 and stack ==1 and priorq ==1:
            print("impossible")
        else:
            print("not sure")
        




    except EOFError:
        break