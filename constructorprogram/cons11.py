class student:
	def __init__(Self,n,r,m):
		self.__name=n
		self.__roll=r
		self.__mark=m
	def show(self):
		print("my name=",self.__name)
		print("my rollno=",self.__roll)
		print("my mark=",self.__mark)
	def upadte(self,n,r,m):
		self.__name=n
		self.__roll=r
		self.__mark=m
	def set__name(self,name):
		self.__name=name
	def set__roll(self,roll):
		self.__roll=roll
	def set__mark(self,mark):
		self.__mark=mark
	def get.__name(self):
		return self.__name
	def get.__roll(self):
		return self.__roll
	def get mark(self):
		return self.__mark
	s=student("swagatika",1,90.50)
	s.show()	
	s.upadte("swagatika jena",1,90.50)
	s.show()
	print("my name=",s.get__name(s))
