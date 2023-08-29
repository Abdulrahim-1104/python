#Higher Order Function
def happy():
    print("Im happy")
def sad():
    print("Im sad")
def fun(func):
    func()
    return sad
f=fun(happy)
f()
# Lambda Function - Annonymous Function
hey=lambda x:x*x
print(hey(2))