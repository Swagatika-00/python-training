class person:
    def f1(self):
        print("class person")

class student(person):
    def f2(self):
        print("class student")

class Enginerring(student):
    def f3(self):
        print("class Enginerring")

ob =Enginerring()
ob.f1()
ob.f2()
ob.f3()