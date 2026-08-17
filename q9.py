#program to find the grade of a student based on marks
n = int(input("enter your marks :"))
if(n>100 or n<0):
    print("invalid entry")
else:
    if(n>=90):
     print("grade A")
    elif(n>=80):
        print("grade B")
    elif(n>=70):
        print("grade C")
    elif(n>=60):
        print("grade D")
    else:
        print("grade F")