#for 2 dimensiional array
list=[[1,2,3],[4,5,6],[7,8,9]]
print(list)
print(list[0][2])
#Tuples in python
tuples=(1,2,3,4)
print(tuples)
print(tuples[0])
#tuples[0]=10 comming to this point we cant assign value to tuples
#Dictionaries in python
dic={1:10,2:20,3:30,4:40,5:50}
print(dic)
for i,j in dic.items():
    print(i,end=' ')
    print(j,end=' ')
print("")
for i in dic.keys():
    print(i,end=' ')
dic[6]=60
print("")
print(dic)
#list inside dictionaries
name=['rahim','selva','praveen','naveen']
age=[12,13,15,16]
gender=['m','m','m','m']
dicc={'Names':name,'Ages':age,'Genders':gender}
print(dicc)
#dictionaries inside list
listt=[]
u1={'name':'rahim','age':18,'gender':'M'}
u2={'name':'santhosh','age':17,'gender':'M'}
u3={'name':'suba','age':15,'gender':'F'}
listt.append(u1)
listt.append(u2)
listt.append(u3)
print(listt)
#dictionares inside dictionaries
dics={
    "dics1":{'one':1},
   " dics2":{'two':2},
    "dics3":{'three':3} 
}
print(dics)