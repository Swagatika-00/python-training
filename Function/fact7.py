#local global
x=10
def show():
	x=30
	print(x)
	print(globals()['x'])
show()
"""
30
10
"""