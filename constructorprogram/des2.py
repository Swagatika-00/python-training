class demo:
	def __init__(self):
		print("constructor")
	def __del__(self):
	 	print("destructor")
d1=demo()
d2=demo()
d3=demo()	 	
print("hi")
		"""
		constructor
constructor
constructor
hi
destructor
destructor
destructor
"""