import functools
# Map it is used to modify the list
item=[['tomato',20],['potato',30],['carrot',12]]
fun=lambda item:[item[0],item[1]/2]
lis=list(map(fun,item))
print(lis)
# exercise 1 for map
item1=[('Maths','Anitha',180),('Science','Jessi',190),('Social','Divya',198)]
f1=lambda item1:(item1[0],item1[1],int(item1[2]/2))
map1=list(map(f1,item1))
print(map1)
item2=[72,76,71,82,89]
f2=lambda item2:["even" if item2%2==0 else "odd"]
map2=list(map(f2,item2))
print(map2)
# Filter used to filter the list
item3=[('Maths','Anitha',180),('Science','Jessi',190),('Social','Divya',198)]
f3=lambda items3:items3[2]>180
filter1=list(filter(f3,item3))
print(filter1)
f4=lambda items3:items3[1][0]=='J'
filter2=list(filter(f4,item3))
print(filter2)
# reduce until the list become one element
val=[2,3,4,5,6]
str=['h','e','l','l','0']
sum=functools.reduce(lambda i,j:i+j,val)
joinn=functools.reduce(lambda i,j:i+j,str)
print(sum)
print(joinn)
# List Comprehension
# first suquare of n natural numbers
# syntax - list[expression for item in items]
sum=[x*x for x in range(1,11)]
print(sum)
l=[13,33,30,43,22,45]
ll=[x for x in l if x<=30]
print(ll)
#dictionries comprehension
dic={'rahim':20,'selva':22,'mugil':24,'suriya':18}
d={ key:val for key,val in dic.items() if val>18}
print(d)
lll=[i/2 for i in l]
print(lll)
# Zip function
a1=['rahim','jasra']
a2=[143,143]
a3=[1.43,1.43]
a4=['i','l','o','v','e','i']
zipped=list(zip(a1,a2,a3,a4))
print(zipped)