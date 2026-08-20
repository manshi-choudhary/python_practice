#program to play rock paper scissor with computer
import random
computer= random.choice([1,-1,0])
choice= input("enter your choice :")
youdict={"r":1,"p":0,"s":-1}
reversedict={1:"rock", 0:"paper",-1:"scissor"}
you=youdict[choice]
print(f"computer chose {reversedict[computer]}\nyou chose {reversedict[you]}")
if(computer==you):
    print("draw!")
else:
    if(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 0 and you == -1):
        print("you won !")
    elif(computer == 1 and you == -1):
        print("you lose !")
    elif(computer == -1 and you == 1):
        print("you won !")
    elif(computer == 1 and you == 0):
        print("you won !")
    elif(computer == 0 and you == 1):
        print("you lose !")
    else:
        print("something went wrong!!")