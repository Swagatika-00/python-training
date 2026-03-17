class student:
	def __init__(self,name):
		self.__name=name
	@property
	def name(self): #getter
		return self._name
	@name.setter	
	def name(self,value):#setter
		self.__name=value
	s=Student("swagatika")
	print(s.name)
	s.name="lully"
	print(s.name)	