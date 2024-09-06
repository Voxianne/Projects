import itertools
import string
import os

def Check():
    new = ''
    Num_List = str(input("Give me a list of interger numbers with punctuactions:"))
    for char in Num_List:
        re_place = ''
        if char in string.punctuation:
            new += ' '
        elif char == ' ':
            new += ' '
            continue
        elif not char.isdigit():
            while not re_place.isdigit():
                re_place = str(input("Please give me a interger number, not an a letter or a float...: "))
                new += ' ' + re_place
        else:
            new += char

    Nums = list(map(int, new.split()))
    return Nums


def Permutations():
    List = Check()

    perm = itertools.permutations(List, len(List))
    for i in list(perm):
        print(i)



#################################
#Ask the user if they wish to re-try
#################################
def ReDo():
    Flag = True
    while Flag:
        Rematch = input("Would you like to make a new permutations?[y/n]")
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

    while ReDo(): 
        Permutations()

    pass


if __name__ == '__main__':
    main()
