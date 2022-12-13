def fact(n):
    s=1
    for i in range(1,n):
        s+=s*i
    return  s
p=int(input("Enter the number to find factorial "))
print("Factorial of {} is {} ".format(p,fact(p)))