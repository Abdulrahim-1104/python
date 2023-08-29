# This program explaining the concepts like Method overriding,Multilevel Inhertance,Multiple Inheritance
#classes and object,etc...
from classes import User,Student,Teacher,StdTch
from classVehicle import car,bike
user1=User("Rahim","ajslkdfk")
user2=User("Jasra","dlkfajlsdf")
print(user1.name)
user1.register()
user2.login()
s1=Student("Std","ppopo")
t1=Teacher("Tch","ppor")
s1.register()
t1.register()
print(s1.name)
print(s1.pwd)
print(t1.name)
print(t1.pwd)
car1=car()
car1.ride()
bike1=bike()
bike1.ride()