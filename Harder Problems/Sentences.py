import random
import os


def Create_Noun_List():

    f = open(r'C:\Users\Voxian\Documents\GitHub\Python_Learning\Problems\Harder Problems\nouns.txt')

    with f as file:
        noun_list = file.read()
        Nouns = list(map(str, noun_list.split()))

    f.close()
    return Nouns


def Create_Verb_List():

    f = open(r'C:\Users\Voxian\Documents\GitHub\Python_Learning\Problems\Harder Problems\verbs.txt')

    with f as file:
        verbs = file.read()
        Verbs = list(map(str, verbs.split()))

    f.close()
    return Verbs


def Create_Word_List():

    f = open(r'C:\Users\Voxian\Documents\GitHub\Python_Learning\Problems\Harder Problems\words.txt')

    with f as file:
        words = file.read()
        Words = list(map(str, words.split()))

    f.close()
    return Words


def Generate_Sentence():

    Noun = Create_Noun_List()
    Verb = Create_Verb_List()
    Word = Create_Word_List()

    sentence = '' + str(random.choice(Noun)) + ' ' + str(random.choice(Verb)) + \
        ' ' + str(random.choice(Word)) + \
        random.choice([',', '.', '!', '?', '...'])

    print(sentence,"\n")
    Save()
    return sentence

#################################
#Ask the player/user if they wish to go for an another round!
#################################

def Save():
    Flag = True
    while Flag:
        Rematch = input("Would you like to save it?[y/n]")
        if Rematch.isalpha():
            if Rematch.lower() == 'y':
                Flag = True
                command = 'cls'
                os.system(command)
                f = open("Sentences_to_Remember.txt","a")
                f.write(Generate_Sentence())
                f.write("\n")
                f.close()
                return True
            elif Rematch.lower() == 'n':
                Flag = False
                break
            else:
                print("Wrong input!")
        else:
            print("Wrong input!")
    return False

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


def main():

    Generate_Sentence()
    while Replay():
        Generate_Sentence()
 

    pass


if __name__ == '__main__':
    main()
