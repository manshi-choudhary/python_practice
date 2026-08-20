#user vs computer hiscore game
import random

def game():
    print("you are playing")
    computer = random.randint(1,100)
    you= int(input("enter your score :"))
    with open("hiscore.exe","r") as f:
        hiscore= f.read()
        if(hiscore!=""):
            hiscore= int(hiscore)
        else:
            hiscore= 0

    print(f"your score : {you}\ncomputer score : {computer}")
    if(you>computer and you>hiscore):
        with open("hiscore.exe","w") as f:
            hiscore= f.write(str(you))
            print("you just scored the hiscore!!")
    elif(computer>you and computer>hiscore):
        with open("hiscore.exe","w") as f:
            hiscore= f.write(str(computer))
            print("computer has just scored the hiscore!!")

game()


    