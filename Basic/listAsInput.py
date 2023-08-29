user_input = input("Enter a list of numbers separated by spaces: ")
print(user_input)
numbers =[int(x)for x in user_input.split()]
print("The list of numbers is:", numbers)