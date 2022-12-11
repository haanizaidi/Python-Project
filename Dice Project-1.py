import random
x=int(input("enter a number 1-6: "))
s=0
again = True
if 1<=x<=6:
    while again:
        b=random. randint(1, 6)
        print("Dice:",b)
        if b==x:
            s+=1
        else:
            pass
        another_roll = input ("Want to roll the dice again? (y/n): ")
        if another_roll.lower() =="y":
            continue
        else:
            break
else:
    print("enter a number between 1-6!!")
print("Total Score: ",s)
print("Thanks for playing!!")
