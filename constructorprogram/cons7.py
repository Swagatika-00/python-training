#one object data take from keyboard using parameter constructor
class demo:
	def __init__(self,x,y):
		self.x=x
		self.y=y#instance variable
print("enter two values")
ob=demo(int(input()),int(input()))
print("display first object values ")
print(ob.x,ob.y)		
"""
enter two values
5
8
display first object values 
5 8
"""