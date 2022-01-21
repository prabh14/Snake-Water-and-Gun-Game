import random

print('''Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.

In situations where both players choose the same object, the result will be a draw.

In the game,
s represents snake
w represents water
g represents gun
\n''')
while True:
    
        def game(computer, player):
            if (computer =="s" and player=="g"):
                return True
            elif(computer=="w" and player=="s"):
                return True
            elif(computer=="g" and player=="w"):
                return True
            elif (computer==player):
                return None

        choices=['s', 'w', 'g']
        computer=random.randint(0,2)
        computer=choices[computer]
        player=input("Choose either s,w or g:\n")
        print("\n")

        win=game(computer,player)
        print(f"You chose {player} and the computer chose {computer}.")


        if win is True:
            print("You won\n","\n")
        elif win is None:
            print("The match is draw.","\n")
        else:
            print("You lost.","\n")
            