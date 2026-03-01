def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
s=0
print("enter min range to max range")
min=int(input())
max=int(input())
for i in range (min,max+1,1):
	s=s+facttest(i)
print("sum=",s)	
"""
enter min range to max range
5
9
sum= 409080
"""