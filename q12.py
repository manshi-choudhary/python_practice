#program to check whether a character is vowel or consonent
w=input("enter a character : ")
if(len(w)==1):
    q=w.lower()
    if(q=='a' or q=='e' or q=='o' or q=='i' or q=='u'):
        print("its a vowel")
    else:
        print("its a consonent")
else:
    print("write only one letter")