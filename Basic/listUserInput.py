list=[]
num=int(input("Enter number of elements"))
while True:
    if num==0:
        break
    list.append(int(input()))
    num-=1
print(list)