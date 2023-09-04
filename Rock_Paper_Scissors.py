# rock papper scissors
print("Welcome in rock/papper/scissors!")

while True:
    print("1 - play")
    print("2 - exit")
    chose = input("Select option: ")


    if chose == '1':
        name1 = input("Enter name's of the player one: ")
        name2 = input("Enter name's of the player two: ")

        player1 = input("Player 1: Choose rock, paper, or scissors: ")
        player2 = input("Player 2: Choose rock, paper, or scissors: ")

        if  (player1 == 'rock' and player2 == 'scissors') or \
                (player1 == 'papper' and player2 == 'rock') or \
                (player1 == 'scissors' and player2 == 'papper'):
            print(name1,"Wins!!!")
        else:
            print(name2,"Wins!!!")

    if chose == '2':
        print("Good bye!!!")
        break

