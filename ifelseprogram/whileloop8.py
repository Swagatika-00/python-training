i=1
print("A")
while i<4:
	print("B")
	i=i+1
	if i==3:
		continue
	print(i)
	print("C")
print("D")
print(i)	
"""
A
B
2
C
B
B
4
C
D
4
"""