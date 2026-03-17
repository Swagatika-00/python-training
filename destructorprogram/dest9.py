#adding two user defined complex number
class Mycomplex:
	def __init__(self,r,i):
		self.r=r
		self.i=i
c1=Mycomplex(2,4)
c2=Mycomplex(3,5)
#c3=c1+c2error
c3=Mycomplex(0,0)
c3.r=c1.r+c2.r
c3.i=c1.i+c2.i
print(c1.r,"+",c1.i,"i")
print(c2.r,"+",c2.i,"i")
print(c3.r,"+",c3.i,"i")
"""
2 + 4 i
3 + 5 i
5 + 9 i
"""
			

		
