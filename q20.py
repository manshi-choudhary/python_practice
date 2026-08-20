n= int(input("enter a number :"))
sum=0
while n>0:
    sum = n%10 +sum
    n= n//10
print(f"Sum of digits of the number is {sum}")