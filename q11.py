#calculator program to perform basic operations
a = int(input("enter a number :"))
b = int(input("enter a number :"))

n = input("chose.... \nsum(s)\nminus(m)\nproduct(p)\ndivision(d)\nexit(e) \nto be performed :")
while(n!= 'e'):
    if(not(n=='s' or n=='p' or n=='d' or n=='m')):
        print("invalid choice try again!!")
    else:
        if(n=='s'):
            print(f"the sum of {a} and {b} is {a+b}")
        elif(n=='m'):
            print(f"the subtraction of {a} and {b} is {a-b}")
        elif(n=='p'):
            print(f"the product of {a} and {b} is {a*b}")
        elif(n=='d'and b!=0):
            print(f"the division of {a} and {b} is {a/b}")
        else:
            print("ERROR!....can't divide by zero")
    n = input("****chose again.... \nsum(s)\nminus(m)\nproduct(p)\ndivision(d)\nexit(e) \nto be performed :")