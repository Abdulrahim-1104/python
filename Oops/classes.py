class User:
    def __init__(self,name,pwd):
        self.name=name
        self.pwd=pwd
    def register(self):
        print("Just wait a minute "+self.name+" we are registering...")
    def login(self):
        print("Welcome "+self.name+" you logged in...")
class Student(User):
    def register(self):#method overriding
        print("Registering as student")
class Teacher(User):#multilevel inheritance
    def register(self):#method overriding
        print("Registering as Teacher")
class StdTch(Teacher,Student): #multiple inheritence
    pass