#way3 take input from keyboard
L=[0,0,0],[0,0,0]
print("enter",len(L)*len([0]),"element")
for i in range(0,len(L),1):
    for j in range(0,len([i]),1):
        L[i][j]=int(input())
print("element are")
for i in range(0,len(L),1):
    for j in range(0,len(L[i]),1):
        print(L[i][j],end="\t")
    print()            
    """
    enter 2 element
5
9
element are
5	0	0	
9	0	0	
"""