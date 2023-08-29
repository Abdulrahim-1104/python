#while looop exercise
letter=' '
while not letter.isalpha():
    letter=input("Enter your name")
print("Your name is "+letter)
#printing 1 to 100 using while loop
i=1
while i<=100:
    if i % 2 == 0:
        print(str(i) + " is an even number")
    else:
        print(str(i) + " is an odd number")
    i+=1
