import random

def main():

    print("Rock Paper Scissors")
    print(" ")

    Components = ['paper','rock','scissors']
    Player_Score = 0
    Bot_Score = 0

    while 1:
        ###############################
        #Create a menu
        ###############################
        print("-> Rock")
        print("-> Paper")
        print("-> Scissors")
        print("-> Exit")

        Players_Choice = input("Please choose:")


        if Players_Choice.lower() == 'r' or Players_Choice.lower() == 'p' or Players_Choice.lower() == 's':
            Bot_Choice = Components[random.randint(0, 2)]
            ###############################
            #Draw
            ###############################
            if Players_Choice.lower() == Bot_Choice:
                print(Players_Choice,"vs", Bot_Choice,"! And it's a Draw!")
                print(" ")

            ###############################
            #In case player chooses scissors
            ###############################
            elif Players_Choice.lower() == 's':
                if Bot_Choice == 'rock':
                    print(Players_Choice, "vs", Bot_Choice, "! And Bot Wins!!")
                    print(" ")
                    Bot_Score += 1

                if Bot_Choice == 'paper':
                    print(Players_Choice, "vs", Bot_Choice, "! And Player Wins!!")
                    print(" ")
                    Player_Score += 1


            ###############################
            #In case player chooses paper
            ###############################
            elif Players_Choice.lower() == 'p':
                if Bot_Choice == 'rock':
                    print(Players_Choice, "vs", Bot_Choice, "! And Player Wins!!")
                    print(" ")
                    Player_Score += 1
                if Bot_Choice == 'scissors':
                    print(Players_Choice, "vs", Bot_Choice,"! And Bot Wins!!")
                    print(" ")
                    Bot_Score += 1

            ###############################
            #In case player chooses rock
            ###############################
            elif Players_Choice.lower() == 'r':
                if Bot_Choice == 'scissors':
                    print(Players_Choice, "vs", Bot_Choice,"! And Player Wins!!")
                    print(" ")
                    Player_Score += 1
                    
                if Bot_Choice == 'paper':
                    print(Players_Choice, "vs", Bot_Choice, "! And Bot Wins!!")
                    print(" ")
                    Bot_Score += 1

        ###############################
        #In case player chooses Exit
        ###############################
        elif Players_Choice.lower() == 'exit':
            if Player_Score > Bot_Score:
                print(" ")
                print("Game Over. Player Wins!!!")
            elif Bot_Score > Player_Score:
                print(" ")
                print("Game Over. Bot Wins!!!")
            else:
                print(" ")
                print("Aaaand it's a Draw!!")
            print(" ")
            print("Thank you for playing!!! :)")
            break

        ###############################
        #In case the input does NOT match the program's criteria
        ###############################
        else:
            continue

if __name__=='__main__':
    main()
