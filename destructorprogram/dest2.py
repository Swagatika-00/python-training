#local object
class demo:
	def __init(self):
		print("constructor")
	def __del(self):
		print("destructor")
def show():
	print("A")
	d1=demo()
print("main start")
show()
print("main end")	
"""
main start
A
main end
"""		