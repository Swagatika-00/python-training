# Parent class
class person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child class
class student(person):
    def _init_(self, name, age, roll):
        super()._init_(name, age)   # calling person constructor
        self.roll = roll

    def show_student(self):
        print("Roll No:", self.roll)


# Grand child class
class EnggStudent(student):
    def _init_(self, name, age, roll, branch):
        super()._init_(name, age, roll)   # calling student constructor
        self.branch = branch

    def show_engg(self):
        print("Branch:", self.branch)


# Object creation
e = EnggStudent("Rahul", 20, 101, "Computer Science")

# Calling methods
e.show_person()
e.show_student()
e.show_engg()