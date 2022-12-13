d={1:34,4:56,2:78,3:89}
# l=[]
# for i in sorted(d.values(),reverse=True):
#     l.append(i)
# print("The list in descending order {}".format(l))
# l=[]
# for i in sorted(d.values()):
#     l.append(i)
# print("The list in Ascending order {}".format(l))

d={1:34,4:56,2:78,3:89}
print('Original dictionary : ',d)
l=list(d.items())
l.sort()
print('Ascending order is ',l)
dict=dict(l)
print("Dictionary ",dict)
# l=list(d.items())
# l.sort(reverse=True)
# print('Descending order is ',l)
# dict=dict(l)
# print("Dictionary ",dict)