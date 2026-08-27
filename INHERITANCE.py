class Person:
    def __init__(self):
        self.name="Apeksha"
        self.age=18
        self.address="Mangalore"
    def eat(self):
        print("I can eat!")
    def sleep(self):
        print("I can sleep!")
    def talk(self):
        print("I can talk!")


#PERSON OBJECT(PARENT)
'''
p1=Person()
print(p1.name,p1.address,p1.age)
p1.sleep()
p1.eat()
p1.talk()
'''
#STUDENT OBJECT(CHILD)
# parent's attributes and methods only
'''
class Student(Person) :         
    pass
std=Student()
print(f"Name :{std.name} ,Age : {std.age},Address : {std.address}") #name,address,age-> Person attributes
std.talk()
std.sleep()
std.eat()
'''

# student attributes and methods
# 1) override parent attributes and methods
'''
class Student(Person) :         
    def __init__(self):
        self.name="Baba Kesari"
    def eat(self):
        print("I can eat muesli!")
std=Student()
print(std.name)
std.eat()
std.sleep()
'''

# 2) add new child attributes+methods other than parent attributes+methods
'''
class Student(Person) :         
    def __init__(self):
        self.friends=25
        self.school="ABC"
    def study(self):
        print("I study!")
print(std.school,std.friends)
std=Student()
std.study()
std.eat() # error!!! new attribute/method defined so parent attribute/method cannot be accesed directly
'''

# existing parent attribute/method + new child attribute/method
'''
class Person:
    def __init__(self,dob):
        self.dob=dob
        self.name="Apeksha"
        self.age=18
        self.address="Mangalore"
    def eat(self):
        print("I can eat!") 
    def sleep(self):
        print("I can sleep!")
    def talk(self):
        print("I can talk!")
class Student(Person) :         
    def __init__(self,DOB):
        super().__init__(DOB)
        self.friends=25
        self.school="ABC"
    def study(self):
        super().eat()
        print("I study!")
std=Student("27-11-2007")
std.study()
print(std.name,std.age,std.address)
print(std.dob)
'''
