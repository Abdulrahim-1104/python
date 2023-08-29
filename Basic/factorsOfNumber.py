#find the n numbers of factors
num=int(input("Enter the number to find factors :"))
list=[]
for i in range(1,num+1):
    if num%i==0:
       list.append(i)
print(list)
