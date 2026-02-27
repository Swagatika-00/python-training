def facttest():
	print("enter a number")
	no=int(input())
	f=1
	while no>0:
		f=f*no
		no=no-1
	print("factorial=",f)
facttest()
facttest()		
"""
enter a number
8
factorial= 40320
enter a number
3
factorial= 6
"""