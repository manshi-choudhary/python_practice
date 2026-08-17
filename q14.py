#program to calculate electricity bill based on units consumed
a = int(input("enter the no. of units consumed :"))
if(a<0):
    print("invalid entry")
else:
    if(a<=100):
        print(f"the bill of {a} units is {a*5}rupees")
    elif(a<=200):
        print(f"the bill of {a} units is {500 + (a-100)*7} rupees")
    elif(a<=300):
        print(f"the bill of {a} units is {1200 + (a-200)*10} rupees")
    else:
        print(f"the bill of {a} units is {2200 + (a-300)*12} rupees")