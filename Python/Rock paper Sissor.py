# playing with computer
import random
x=0
y=0
over = False
print("\n ********** ROCK PAPER SISSOR ********** \n")
print("The game will be of best of 3, Any player who manages to score 2 points first will be considered as the winner of the game. \n Thank you! ")
while over!=True:
        PC=random.randint(1,3)
        # 1=rock
        # 2=paper
        # 3=sissor
        Player=input("Player Enter Rock(R), Paper(P) or Sissor(S): ")
        if PC==1 and Player=="r":
                print("PC Choosed ROCK")
                print("Draw!")
                print("\n")
        elif PC==2 and Player=="p":
                print("PC Choosed PAPER")
                print("Draw!")
                print("\n")
        elif PC==3 and Player=="s":
                print("PC Choosed SISSOR")
                print("Draw!")
                print("\n")
        elif(PC==1 and Player=="p"):
                print("PC Choosed ROCK")
                print("Player won the round! ")
                y=y+1
                print("PC score =",x)
                print("Player score =",y)
                print("\n")
        elif(PC==1 and Player=="s"):
                print("PC Choosed ROCK")
                print("PC won the round!! ")
                x=x+1
                print("PC score =",x)
                print("Player score =",y)
                print("\n")
        elif(PC==2 and Player=="r"):
                print("PC Choosed PAPER")
                print("PC won the round!! ")
                x=x+1
                print("PC score =",x)
                print("Player score =",y)
                print("\n")
        elif(PC==2 and Player=="s"):
                print("PC Choosed PAPER")
                print("Player won the round!! ")
                y=y+1
                print("PC score =",x)
                print("Player score =",y)
                print("\n")
        elif(PC==3 and Player=="r"):
                print("PC Choosed SISSOR")
                print("Player won the round!! ")
                y=y+1
                print("PC score =",x)
                print("Player score =",y)
                print("\n")
        elif(PC==3 and Player=="p"):
                print("PC Choosed SISSOR")
                print("PC won the round!! ")
                x=x+1
                print("PC score =",x)
                print("Player score =",y)
                print("\n")
        else:
                print("you entered different, Please enter the option correctly")
        
        if x==2:
                print("Pc won the game")
                over=True
                print("**** GAME OVER ****")
                print("\n")
        elif(y==2):
                print("Player won the game")
                over=True
                print("**** GAME OVER ****")
                print("\n")

    
        
    

        
                
                