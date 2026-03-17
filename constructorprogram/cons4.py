#two object creation
class demo:
	def __init__(self):
		self.x=10
		self.y=20#instance variable
ob=demo()
print(ob.x)
print(ob.y)
ob1=demo()
print(ob.x)
print(ob.y)		
"""
10
20
10
20
"""