import random
import os

###################################
#Comparing the bot's number with the user input and returns the results
###################################


def Cows_and_Bulls(player_number, bot_number):
    cows = 0
    bulls = 0
    digit_bot = []
    digit_bot[:] = bot_number

    digit_player = []
    digit_player[:] = player_number

    for i in range(len(digit_player)):
        for j in range(len(digit_bot)):
            if digit_player[i] == digit_bot[j]:
                if i == j:
                    bulls += 1
                else:
                    cows += 1
    return cows, bulls


###################################
#Main Structure of the Game
###################################
def Game():
    command = 'cls'
    os.system(command)

    attempts = 5
    bot_choice = ''
    while not len(bot_choice) > 3:
        bot_number = random.randint(0, 9)
        bot_choice = bot_choice + str(bot_number)
        
    print("You may only add two digit number!")

    while 1:
        player_choice = str(input("Please take your guess:"))

        if player_choice.isdigit():
            if not len(player_choice) != 4:
                if attempts > 1:
                    cows, bulls = Cows_and_Bulls(player_choice, bot_choice)
                    if bulls == 4:
                        print(" ")
                        print("Player Wins!")
                        break
                    else:
                        print("Player has", cows, "cows and", bulls, "bulls!")
                        attempts -= 1
                        print("")
                        print(attempts, "remaining!")
                else:
                    print(" ")
                    print("Game Over!The number was:", bot_choice)
                    break


###################################
#Check wether the player wants to play again or not
###################################
def Replay():
    Flag = True
    while Flag:
        Rematch = input("Would you like to play?[y/n]")
        if Rematch.isalpha():
            if Rematch.lower() == 'y':
                Flag = True
                command = 'cls'
                os.system(command)
                return True
            elif Rematch.lower() == 'n':
                Flag = False
                break
            else:
                print("Wrong input!")
        else:
            print("Wrong input!")
    return False


###################################
#While Replay() is True, continue playing
###################################
def main():

    while Replay():
        Game()
    print("Exiting...")


if __name__ == '__main__':
    main()
