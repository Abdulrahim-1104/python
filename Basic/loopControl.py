# break pass continue
#This is for continue
question="1,2,3,4,5"
answer=""
for i in question:
    if i==',':
        continue
    answer+=i
print(answer)
#This is for break
n=int(input("Enter the number"))
list = []
for i in range(1,n+1):
    if 20%i==0:
        list.append(i)
print(list)