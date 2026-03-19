#delete odd store only even no. in same list
L=[10,20,30,40,50,13,67]
L=[x for x in L if x %2==0]
print(L)
"""
[10, 20, 30, 40, 50]
"""