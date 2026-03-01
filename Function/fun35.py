def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
#s=facttest (3)+facttset (4)+facttest(5)
s=0
for i in range(3,6,1):
		s=s+facttest(i)
print("3!+4!+5!=",s)	
"""
3!+4!+5!= 150
"""