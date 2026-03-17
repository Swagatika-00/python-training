#parent class
class person:
	def __init(self,name,age):
		self.name=name #property
		self.age=age
	def show_person(self):#method
		print("Name:",self.name)
		print("Age:",self.age)	

#child class
class student(person):
	def __init__(self,name,age,roll):
		super().__init__(name,age)  #calling person constructor
		self.roll=roll
	def show_student(self):
		print("Roll No:",self.roll)
#Grand child class
class EnggStudent(student):
	def __init__(self,name,age,roll,branch):
		super().__init__(name,age,roll)  #calling student constructor
		self.branch=branch
	def show_egg(self):
		print("Branch:",self.branch)

#Object creation
e=EnggStudent("Rahul",20,101,"Computer Science")
#calling methods
e.show_person()
e.show_student()
e.show_egg()		
		

