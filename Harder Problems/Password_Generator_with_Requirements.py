import string
import random
import os


def Password_Generator(number):
    Letter_List = []
    Letter_List[:] = string.ascii_letters
    Letter_List[:] += string.digits
    Letter_List[:] += string.punctuation

#############################################
#   A faster way to make the list and add all the required strings
#    Letters = ''
#    Letters = string.ascii_letters + string.digits + string.punctuation
##############################################
    while 1:
        G_Password = ''
        lower = 0
        upper = 0
        num = 0
        special = 0
        for i in range(number):
            G_Password += random.choice(Letter_List)
        for char in G_Password:
            if char in string.ascii_lowercase:
                lower += 1
            elif char in string.ascii_uppercase:
                upper += 1
            elif char in string.digits:
                num += 1
            elif char in string.punctuation:
                special += 1
        if lower != 0 and upper != 0 and num !=0 and special !=0:
            break 
    print("The new password is:", G_Password)

#################################
#Ask the user if they wish to re-generate a password
#################################


def ReDo():
    Flag = True
    while Flag:
        Rematch = input("Would you like to generate an another password?[y/n]")
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

############################################
#Main function
############################################


def main():

    pass_length = 0
    while pass_length < 4:
        pass_length = int(input("How long should the password be: "))
    Password_Generator(pass_length)
    while ReDo():
        Password_Generator(pass_length)
    print("Exiting Password_Generator.py...")


if __name__ == '__main__':
    main()
