#wap take emp salary from keyboard if sal>=5000

print("enter basic salary")
sal=float(input())
da,hra=0,0
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
	totalsal=sal+da+hra
	print("basic sal=",totalsal)
	print("da=",totalsal)
	print("hra=",totalsal)
	print("total salary=",totalsal)

"""
enter basic salary
6000
basic sal= 9000.0
da= 9000.0
hra= 9000.0
total salary= 9000.0
"""
