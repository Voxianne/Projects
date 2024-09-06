
def Swappies_WayOne(number_one,number_two):
    number_swap = number_one
    number_one = number_two
    number_two = number_swap
    return number_one,number_two

def Swappies_Shortcut(number_one,number_two):
    number_one,number_two = number_two, number_one
    return number_one,number_two


def main():
    number_one = int(input("Gimme one number and i shall grant you the ability to give me one more! :"))
    number_two = int(input("Now, gimme the second and i shall show you a smol trick!: "))

    print("Now lemme show you the magic with the help of a friend from Swappies_WayOne, and with them we shall have le numbers swapped!")
    print("The first number was: ", number_one," and the second: ", number_two, " !")
    print("Abracatabra!Now they are!", Swappies_WayOne(number_one,number_two))

    print("Now lemme show you the magic from Swappies_Shortcut, and with it we shall have le numbers swapped again!")
    print("The first number was: ", number_one," and the second: ", number_two, " !")
    print("Abracatabra!Now they are!", Swappies_WayOne(number_one,number_two))
    

if __name__ == '__main__':
    main()