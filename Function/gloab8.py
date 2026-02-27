def show():
	x=10
	print("inside show x=",x)
	disp(x)
	print("inside show x=",x)
def disp(x):
	print("inside show x=",x)
print("start")
show()
print("end")
"""
start
inside show x= 10
inside show x= 10
inside show x= 10
end
"""