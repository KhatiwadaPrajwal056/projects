# Multiplayer 

import random
pc=random.randrange(1,4)
print(pc)

x=0
y=0
over = False
print("\n ********** ROCK PAPER SISSOR ********** \n")
print("The game will be of best of 3, Any player who manages to score 2 points first will be considered as the winner of the game. \n Thank you! ")
while over!=True:
    p1=input("P1 Enter Rock(R), Paper(P) or Sissor(S): ")
    p2=input("P2 Enter Rock(R), Paper(P) or Sissor(S): ")
    if p1=="r" and p2=="r":
        print("Draw!")

        print("\n")
    elif p1=="p" and p2=="p":
        print("Draw!")
        print("\n")
    elif p1=="s" and p2=="s":
        print("Draw!")
        print("\n")
    elif(p1=="r" and p2=="p"):
        print("P2 won the round! ")
        y=y+1
        print("P1 score =",x)
        print("P2 score =",y)
        print("\n")
    elif(p1=="r" and p2=="s"):
        print("P1 won the round!! ")
        x=x+1
        print("P1 score =",x)
        print("P2 score =",y)
        print("\n")
    elif(p1=="p" and p2=="r"):
        print("P1 won the round!! ")
        x=x+1
        print("P1 score =",x)
        print("P2 score =",y)
        print("\n")
    elif(p1=="p" and p2=="s"):
        print("P2 won the round!! ")
        y=y+1
        print("P1 score =",x)
        print("P2 score =",y)
        print("\n")
    elif(p1=="s" and p2=="r"):
        print("P2 won the round!! ")
        y=y+1
        print("P1 score =",x)
        print("P2 score =",y)
        print("\n")
    elif(p1=="s" and p2=="p"):
        print("P1 won the round!! ")
        x=x+1
        print("P1 score =",x)
        print("P2 score =",y)
        print("\n")
    else:
        print("you entered different, Please enter the option correctly")
    
    if x==2:
        print("Player 1 won the game")
        over=True
        print("**** GAME OVER ****")
        print("\n")
    elif(y==2):
        print("Player 2 won the game")
        over=True
        print("**** GAME OVER ****")
        print("\n")

    
        
    
