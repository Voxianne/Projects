def Maxxie_Max_WayOne(number_one, number_two):
    if number_one>number_two:
        return number_one
    elif number_two>number_one:
        return number_two
    else:
        return 0

def Maxxie_Max_Shortcut(number_one,number_two):
    if max(number_one,number_two) != 0:
        return max(number_one, number_two)
    else:
        return 0

def main():
    number_one = int(input("Sire/Ma'am! Give me test subject number one!: "))
    number_two = int(input("Great!Now onto test subject number two!: "))

    if Maxxie_Max_WayOne(number_one,number_two) != 0:
        print("Hmmm....Results from Maxxie_Max_WayOne show that the largest test subject of two is: ", Maxxie_Max_WayOne(number_one,number_two))
    else:
        print("I want other test subjects...These ones won't do....")
    
    if Maxxie_Max_Shortcut(number_one,number_two) == 0:
        print("Hmmm....Results from Maxxie_Max3_Shortcut show that the largest test subject of two is...: ", Maxxie_Max_Shortcut(number_one,number_two))
    else:
        print("I want other test subjects...These ones won't do eitherrrrr....")    

if __name__ == '__main__':
    main()