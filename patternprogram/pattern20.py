
for i in range(4,0,-1):
	for j in range(1,i+1,1):
		print(j,end="\t")
	for j in range(i,0,-1):
		print(j,end="")
	print()		
for i in range(1,5,1):
	for j in range(1,i+1,1):
		print(j,end="\t")
	for j in range(i,0,-1):
		print(j,end="")
	print()	
	"""
	1	2	3	4	4321
1	2	3	321
1	2	21
1	1
1	1
1	2	21
1	2	3	321
1	2	3	4	4321
"""
