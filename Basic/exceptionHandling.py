new=int(input("Enter the numerator"))
deno=int(input("Enter the denominator"))
try:
    result=new/deno
    print(result)
except Exception:
    print("Please enter correct value or if you enterted the denomenator as zero then please change it")