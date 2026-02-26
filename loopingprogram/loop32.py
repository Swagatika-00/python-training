#simple interest
def sican(p, r, t):
    si = (p * r * t) / 100
    print("Simple Interest is:", si)

# Taking input
principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of interest: "))
time = float(input("Enter Time (in years): "))

sican(principal, rate, time)
"""
Enter Principal amount: 4000
Enter Rate of interest: 15
Enter Time (in years): 2
Simple Interest is: 1200.0
"""