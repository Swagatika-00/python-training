#take 20 list data from keyboard no.1 way
L=[]
print("enter how many list store")
s=int(input())
for i in range(0,s,1):
	print("enter list1 data")
	x=eval(input())
	L.append(x)
print("elements are")
for i in range(0,len(L),1):
	for j in range(0,len(L[i]),1):
		print(L[i][j],end="\t")
	print()	
	"""
	enter how many list store
2
enter list1 data
[2,4,6]
enter list1 data
[2,9]
elements are
2	4	6	
2	9	
"""