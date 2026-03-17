#create private method
class demo:
	def __init__(self):#private method
		print("hi")
	def disp(self):#public method
		self.__show()
ob=demo()
#ob.__show()error
ob.disp()		