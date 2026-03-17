#passing object reference in argument
class Student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
	def show(s):
		print("my name=",s.name)
		print("my rollno=",s.roll)
		print("my mark=",s.mark)
s=Student("swagatika",1,90.50)
s.show()	
"""
my name= swagatika
my rollno= 1
my mark= 90.5
"""