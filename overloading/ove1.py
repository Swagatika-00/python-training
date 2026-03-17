class Demo:
	def show(self,a=0,b=0):
	   print("two argument show",a,b)
d=Demo()
d.show()
d.show(10,20)
d.show(5)	
"""
two argument show 0 0
two argument show 10 20
two argument show 5 0
"""
