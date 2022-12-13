l=str(input("Enter the text"))
k=list(set(l.split()))
for i in k:
    print("{} find {} times".format(i,l.count(i)))