#Take a list at the keyboard
L=[]
print("enter how many datastore in list")
s=int(input())
for i in range(0,s,1):
	print("enter element",i+1)
	L.append(int(input()))
print(L)	