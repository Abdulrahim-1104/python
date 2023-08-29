# If else and elif and ladder exercise
a=int(input("Enter the value for a "))
b=int(input("Enter the value for b "))
      # if else
if a%2==0 and b%2==0:
    print("Both are even number ")
else :
    print("Not both are even number")
#elif
if a>b:
     print("A is greater than B")
elif b>a:
     print("B is greater than A")
else:
     print("A and B both are equal")
     # if else ladder
if a>b:
     print("A is greater than B")
     if a%2==0:
         print("And A is a even number")
     else:
         print("And A is a odd number")
elif b>a:
     print("B is greater than A")
     if b%2==0:
         print("B is a even number")
     else:
         print("B is a odd number")
else:
     print("A and B both are equal")
     if a%2==0 and b%2==0:
         print("Both are even number")
     elif a%2==0:
         print("A is even and B is odd")
     elif b%2==0:
         print("B is even and A is odd")
     else:
         print("Both are odd number")
