#2nd way
L=[]
print("enter how many list store")
s=int(input())
for i in range(0,s,1):
	x=[]
	print("enter list",i+1,"how many data")
	s1=int(input())
	for j in range(0,s1,1):
		print("enter element",j+1)
		x.append(int(input()))
	L.append
print("elements are")
for i in range(0,len(L),1):
    for j in range(0,len(L[i]),1):
    	print(L[i][j],end="\t")
    print()		
    """
    enter how many list store
2
enter list 1 how many data
3
enter element 1
10
enter element 2
20
enter element 3
30
enter list 2 how many data
2
enter element 1
40
enter element 2
50
elements are
10    20    30
40    50
"""