#Return object reference
class student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
	def show(self):
		s=student("lully",1,90.50)
		return s
obj=student("temp",0,0)		
res=obj.show()
#print(type(res),res)
print("my name=",res.name)		
print("my rollno=",res.roll)
print("my mark=",res.mark)
"""
my name= lully
my rollno= 1
my mark= 90.5
"""
