def getfib(j):
    n1=1
    n2=1
    if j<=2:
        if j==1:
            l=[n1]
        else:
            l=[n1,n2]
    else:
        l=[n1,n2]
        count = 2
        while count < j:
            nth = n1 + n2
            l.append(nth)
            n1 = n2
            n2 = nth
            count += 1
    print(l)

k=int(input("Enter the number"))
getfib(k)