#constructor use to initialise the instance variable using method
class demo:
	def set(self,x,y):#method
		self.x=x
		self.y=y#instance variable
print("enter two values")
ob=demo()
ob.set(10,20)
print("display first object values")
print(ob.x,ob.y)		
		"""
		enter two values
display first object values
10 20
"""