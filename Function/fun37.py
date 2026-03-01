def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
s1=""
for i in range(min,max+1,1):
	s=s1+strtest(i)
	s=s+facttest(i)
print(s1,"\b=",s,sep="")
