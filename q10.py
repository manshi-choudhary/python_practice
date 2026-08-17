#program to check whether a year is leap year or not
n = int(input("enter an year :"))
if((n%400==0) or (n%4==0 and n%100!=0)):
    print("a leap year")
else:
    print("a regular year")