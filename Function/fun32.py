def cal(no1,no2):
	return no1+no2,no1-no2,no1*no2,no1/no2
print("enter two nos")
no1=int(input())
no2=int(input())
a,s,m,d=cal(no1,no2)
print("sum=",a)
print("mult=",m)
print("sub=",s)
print("div=",d)
"""
enter two nos
6
7
sum= 13
mult= 42
sub= -1
div= 0.8571428571428571
"""
