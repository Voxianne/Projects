import os
import random

###########################################
#Using the Ascii Hangman images, one for each failed attempt until attempt == 7
###########################################
def Hangman(attempts_left):

    hangman_list = ['''
                    +---+
                    |   |
                        |
                        |
                        |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                        |
                        |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                    |   |
                        |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                   /|   |
                        |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                        |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                   /    |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                   / \  |
                        |
                    =========''']

    if attempts_left < (len(hangman_list)):
        print(hangman_list[attempts_left])
        return attempts_left


###########################################
#Slice per letter the chosen and the display word and compare the chosen word's
#letters with letter
#if condition is true then replace the hyphen in D_List[i] with letter and add the letters back
#in new variable new_display_word
#Also, call Hangman() function and increase attempt by 1
###########################################
def Compare_Words(chosen_word,display_word,letter,attempt):

    Chosen_List = []
    Chosen_List[:] = chosen_word

    D_List = []
    D_List[:] = display_word

    counter = 0
    for i in range(len(Chosen_List)):
        if Chosen_List[i] == letter:
            if D_List[i] != letter:
                D_List[i] = letter
                counter +=1
    if counter == 0:
        Hangman(attempt)
        attempt +=1
    
    new_display_word = ''
    for i in range(len(Chosen_List)):
        new_display_word += D_List[i] 
    return new_display_word,attempt


#################################
#Takes a random word from word_bank,makes the necessary changes so that only the first letter appears and
#the rest are replaced with '_'
#################################
#Asks for user input and starts comparing till attempts == 7  or the word is found
#################################
def Game():

    f = open(r'C:\Users\Voxian\Documents\GitHub\Python_Learning\Problems\Medium problems\Simple Games\Word_List.txt')

    with f as file:
        word_list = file.read()
        Words = list(map(str, word_list.split()))
    chosen_word = random.choice(Words)

    f.close()

    display_word = chosen_word[0]
    for char in chosen_word[0:]:
        display_word +=  '_'
    print("Find the word!")

    print("")
    for char in display_word:
        print(char,end= ' ')
    
    attempt = 0
    while 1:
        Given_Letter = input("\nLetter: ")
        if Given_Letter.isalpha() and len(Given_Letter) == 1:
            letter = Given_Letter.lower()
            display_word,attempt = Compare_Words(chosen_word,display_word,letter,attempt)
            if attempt == 7:
                print("Game Over!The word was:", chosen_word)
                break
            elif display_word == chosen_word:
                print("You win!")
                break
            else:
                if attempt == 0:
                    print("")
                    print(display_word)
                else:
                    print("")
                    print(display_word)
        else:
            print("Wrong input!")

        
#################################
#Ask the player/user if they wish to go for an another round!
#################################
def Replay():
    Flag = True
    while Flag:
        Rematch = input("Would you like to play again?[y/n]")
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


#################################
#Main function that counts on Replay().If Replay() == False, the game exits. Else, another one!
#################################
def main():

    Game()
    while Replay():
        Game()
    print("Exit Game...")




if __name__ =='__main__':
    main()
