# generators is nothing but that return immediately but it return until the condition satisify
# it is used to wastage of memory
def sum(num):
     for i in range(0,num+1):
         yield i*i

print(sum(10))
n=sum(10) # we want to access using any variable by stroing the address variable
for i in n:
    print(i,end=" ")