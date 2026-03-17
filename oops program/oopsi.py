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
i1=simpleinterest(5000,15,3)
i1.show()
print("simple interest=",i1.sical())	    
"""
principle= 5000
rate= 15
time= 3
simple interest= 2250.0
"""