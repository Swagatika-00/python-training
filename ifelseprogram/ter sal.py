print("enter basic salary")
sal=float(input()) 
da=sal*0.3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)   	

"""
enter basic salary
6000
basic sal= 6000.0
da= 1800.0
hra= 1200.0
total salary= 9000.0
"""