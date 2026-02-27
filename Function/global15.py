#even/odd
def check_even_odd():
    num = int(input("Enter a number: "))
    
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

result = check_even_odd()
print(result)
"""
Enter a number: 4
Even Number
"""
