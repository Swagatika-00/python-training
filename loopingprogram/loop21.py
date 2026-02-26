print("A")
for i in range(1,6,1):
	print("B")
	print(i)
	if i>=3:
		continue
	print("C")
print("D")
print(i)		
"""
A
B
1
C
B
2
C
B
3
B
4
B
5
D
5
"""