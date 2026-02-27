def show():
	x=[10]
	disp(x)
	print("inside show x=",x)
def disp(x):
	x.append(40)
print("start")
show()
print("end")	
"""
start
inside show x= [10, 40]
end
"""