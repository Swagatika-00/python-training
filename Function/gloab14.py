#si
def simple_interest():
    p = float(input("Enter Principal: "))
    r = float(input("Enter Rate: "))
    t = float(input("Enter Time: "))
    
    si = (p * r * t) / 100
    return si

result = simple_interest()
print("Simple Interest is:", result)
"""
Enter Principal: 5000
Enter Rate: 12
Enter Time: 2
Simple Interest is: 1200.0
"""