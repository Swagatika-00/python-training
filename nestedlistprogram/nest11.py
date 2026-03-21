#Transpose matrix
L1=[[1,2,3],[4,5,6],[7,8,9]]
L2=[[0,0,0],[0,0],[0,0]]
for i in range(len(L1)):
	for j in range(len(L1[i])):
	    L2[j][i]=L1[i][j]
print(L2)		