#guess the number game
import random

user= random.randint(1,100)
guess = -1
count =0
while guess != user :
    guess=int(input("guess a number :"))
    if(guess == user):
        print("you win!!")
        break
    else:
        if(guess>user):
            print("too high!")
        elif(guess<user):
            print("too low!")
        else:
            print("invalid choice,choose again!")
        count +=1

print(f"the number of counts took place is {count}")