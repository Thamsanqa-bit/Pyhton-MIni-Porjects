name = input("PLease enter your name: ")
print("WEclome to adventure game")

answer = input("You are on a dirt road,would you like to go left or right? ")
if answer == 'left':
    answer = input("You come to the river, do you want to swim or walk across: ")
    if answer == 'swim':
        print("You swam into the alligatotrs and got eaten")
    elif answer == 'walk':
        print("You walked for many miles, you ran out of water and lost the game ")
    else:
        print("Ivalid option, You lose!")

elif answer == 'right':
    answer = input("You came to the bridge do you want to cross or go back(cross/back) ")
    if answer == 'cross':
        print('You crossed over and win a prize!')
    elif answer == 'back':
        print('You chicken out and lose!')
     
    else:
        print("Invalid option, You lose!")
else:
    print("Invalid option, You lose!")
