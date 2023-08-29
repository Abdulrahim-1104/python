list=[-1,-2,-3,0,1,2,3]
sub_list=[]
i=0
while i<len(list):
    if list[i]<0:
        sub_list.append(list.pop(i))
        i-=1
    i+=1
list.extend(sub_list)
print(list)