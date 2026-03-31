n = 4

for i in range(n, 0, -1):
    # increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    
    # spaces
    for j in range(2 * (n - i) - 1):
        print(" ", end="")
    
    # decreasing numbers
    if i != n:
        for j in range(i, 0, -1):
            print(j, end="")
    else:
        for j in range(i - 1, 0, -1):
            print(j, end="")
    
    print() 
    """
    1234321
123 321
12   21
1     1
"""