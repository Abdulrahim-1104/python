#Sorting with key
items=[('Maths','Anitha',80),('Science','Jessi',90),('Social','Divya',98)]
i1=items
i2=items
i3=items
i1.sort(key=lambda items:items[0])
i2.sort(key=lambda items:items[1])
i3.sort(key=lambda items:items[2],reverse=True)
print("Printing sorted list using subject")
print(i1)
print("Print sorted list using name")
print(i2)
print("Printing sorted list using marks")
print(i3)
result = lambda items:items[0]
