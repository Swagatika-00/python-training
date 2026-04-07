#write 3 student record into file
import pickle
#create class
class student:	
	def __init__(self,roll,name,mark):
		self.roll=roll
		self.name=name
		self.mark=mark
	def show(self):
		print(self.roll,self.name,self.mark)
f=open("student.dat","wb")
s1=student(101,"Amit",85)
s2=student(102,"Ravi",90)
s3=student(103,"Sita",88)
pickle.dump(s1, f)
pickle.dump(s2, f)
pickle.dump(s3, f)
f.close()		