# Variable length arguments using single type argument
def product(*a):
    product=1
    for i in a:
        product*=i
    return product
print(product(1,2,3,4,5))
# Variable length arguments using keywords
def usingK(**kargs):
    for i,j in kargs.items():
        print(i,j,end=" ")
        print("")
print(usingK(name="Rahim",age=16,aim="NoAim"))
# Default arguments
def default(name,defa="NoName"):
    print("Welcome "+name+" "+defa)
default(name="rahim")