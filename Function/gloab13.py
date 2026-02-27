#RETRUN VALUE WITH NO ARGUMENT
#factorial number
def factorial():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

result = factorial()
print("Factorial is:", result)
"""
Enter a number: 5
Factorial is: 120
"""