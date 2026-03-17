class simpleinterest:
	def __init__(self,p,r,t):
		self.p=p
		self.rate=r
		self.time=t
	def show(self):
	    print("principle=",self.p)
	    print("rate=",self.rate)
	    print("time=",self.time)
	def sical(self):
	    return self.p*self.rate*self.time/100
print("enter principle rate and time")
#i1=simplefloat(float(input()),float(input()),float()))
pr=float(input())
r=float(input())
t=float(input())
i1=simpleinterest(pr,r,t)
i1.show()	    
print("simple interest=",i1.sical())	  
"""
enter principle rate and time
6000
10
2
principle= 6000.0
rate= 10.0
time= 2.0
simple interest= 1200.0
"""  