#program to find the greatest of three numbers
def greatest():
    a=int(input("enter a number:"))
    b=int(input("enter another number:"))
    c=int(input("enter one another number too:"))
    if(a>=b and a>=c):
        print(f"{a} is greatest")
    elif(b>=a and b>=c):
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")

greatest()
