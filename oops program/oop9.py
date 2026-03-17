class Square:
    def _init_(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# Taking input
side = int(input("Enter the side of the square: "))

# Creating object
s=Square(side)

# Display results
print("Area of square:", s.area())
print("Perimeter of square:", s.perimeter())