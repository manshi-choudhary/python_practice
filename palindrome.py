class Palindrome:
    def ispalindrome(self, x):
        n= int(x)
        original = n
        reverse=0
        while n>0:
            a= n%10
            reverse= reverse*10 +a
            n= n//10
        if(not (original == reverse)):
            return False
        else:
            return True

a= Palindrome()
x= input("enter a number to check :")
print(a.ispalindrome())