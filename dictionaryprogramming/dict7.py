#remove duplicate element in list and order also maintain
L=[5,8,7,9,6,4,5,8]
d1={}
d1=d1.fromkeys(L)
L=list(d1.keys())
print(L)
