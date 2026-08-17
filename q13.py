#program to check whether three sides can form a triangle or not
a = int(input("enter a side of triangle :"))
b = int(input("enter a side of triangle :"))
c = int(input("enter a side of triangle :"))
if((a+b>c and b+c>a and c+a>b) and a>0 and b>0 and c>0):
    print("it can form a triangle")
else:
    print("it can't form a triangle")