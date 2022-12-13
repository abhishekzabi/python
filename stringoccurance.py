
n=int(input("How many names do you want to insert"))
count=0
firstname=[]
for i in range(0,n):
    fnam=input("Enter the name ")
    count+=fnam.lower().count("a")
    firstname.append(fnam)
print(count," times found")