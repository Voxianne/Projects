import random
import os

#################################
#Function of the Game of Word Completion
##################################
def Check_The_Word(Displayed_Word, User_Input):
 
    Length = len(Displayed_Word)
    counter = 0
    #################################
    #Check the specific letters with the help of a flag
    #################################
    for i in Displayed_Word:
        if '_' in i:
            continue
        elif ' ' in i:
            continue
        else:
            counter += 1
    #################################
    #Create two lists to compares the letters of each word with the Desplayed_Word
    #################################
    D_List =[]
    D_List[:] = Displayed_Word

    Check_List = []

    #################################
    #Open Word_List.txt  and copy all its contents in a list, then close the file 
    #to avoid possible changes in it
    #################################
    f = open(r'C:\Users\Voxian\Documents\GitHub\Python_Learning\Problems\Medium problems\Simple Games\Word_List.txt')

    with f as file:
        word_list = file.read()
        #################################
        #map() separates each word and turns it into a string without having \n
        #map() loops through the words and separates them with the help of split, then adding them in a list 
        #################################
        Words = list(map(str, word_list.split())) 
    
    f.close()

    #################################
    #Create a list in which every possible solution is stored
    #################################
    matched_words = []
 
    for x in range(0,len(Words)):
        check = 0
        word = Words[x]
        Check_List[:] = word

        if len(Check_List) == Length:
            for i in range(Length):
                if Check_List[i] == D_List[i]:
                    check += 1
        if check == counter:
            matched_words.append(word)
        Check_List.clear()
 
    #################################
    #Check wether or not the user input matches one of the words in matched_word list
    #################################
    for i in range(len(matched_words)):
        if User_Input == matched_words[i]:
            return True
    return False

#################################
#Take user input, check with hidden word's length and call Check_The_Word()
#################################
def Game():

    f = open(r'C:\Users\Voxian\Documents\GitHub\Python_Learning\Problems\Medium problems\Simple Games\Word_List.txt')
    
    with f as file:
        word_list = file.read()
        Words = list(map(str,word_list.split()))
    chosen_word = random.choice(Words)
    
    f.close()

    display_word = ''
    counter = 0

    for i in chosen_word:
        if counter <= int(len(chosen_word)+1/2):
            if random.randint(0,1) == 1:
                if '\n' not in i:
                    display_word = display_word + i
                    counter +=1
            else:
                if '\n' not in i:
                    display_word = display_word + '_'
                    counter +=1
        else:
            display_word = display_word + i
            counter += 1
   

    
    print("Please complete the word displayed below at most 2 times!")
    print(display_word, "The total number of letters is: ", len(display_word))
    print("")
    print("You have 3 tries!")
    print("")
    fail = 0
    while 1:
        Given_word = input("Checking the word: ")
        if Given_word.isalpha() and len(display_word) == len(Given_word):
            word = Given_word.lower()
            Flag= Check_The_Word(display_word,word)
            if Flag:
                    print("You Win!")
                    break
            else:
                if fail < 2:
                    fail += 1
                    print("Incorrect! You have",3 - fail,"tries remaining!")

                else:
                    print("Game Over!")
                    break

        else:
            print("There was an error processing your answer. Please Try Again.")


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
    print("Exiting...")


if __name__=='__main__':
    main()
