n=(input("enter the number :"))
i=0
for i in range(len(n)):
    if(not(n[i]==n[len(n)-i-1])):
        print("not palindrome")
        break

else:
    print("the number is palindrome")
