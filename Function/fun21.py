#return value with aqrgumeent
def sical(p,t,r):
	si=p*t*r/100
	return si
print("enter principle")	
p=float(input())
print("enter rateof interest")
r=float(input())
print("enter time")

t=float(input())
res=sical(p,r,t)
print("simpleinterest=",res)
"""
	enter principle
6000
enter rateof interest
12
enter time
2
simpleinterest= 1440.0
"""	