#parameter constructor
class demo:
	def __init__(self,x,y):#parameter constructor
		self.x=x
		self.y=y#instance variable
ob=demo(5,7)
ob1=demo(10,20)
print("display first object values")
print(ob.x,ob.y)
print("display second object values")
print(ob1.x,ob1.y)		
"""
display first object values
5 7
display second object values
10 20
"""