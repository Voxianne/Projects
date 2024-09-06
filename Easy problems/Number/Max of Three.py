def Maxxie_Max3_WayOne(number_one, number_two,number_three):
    if number_one>=number_two and number_one>=number_three:
        return number_one
    elif number_two>=number_one and number_two>=number_three:
        return number_two
    elif number_three>=number_one and number_three>=number_two:
        return number_three
    else:
        return 0

def Maxxie_Max3_Shortcut(number_one,number_two,number_three):
        return max(number_one, number_two,number_three)


def main():
    number_one = int(input("Sire/Ma'am! Give me test subject number one!: "))
    number_two = int(input("Great!Now onto test subject number two!: "))
    number_three = int(input("Last but not Least!! Onto test subject number three!: "))

    if Maxxie_Max3_WayOne(number_one,number_two,number_three) != 0:
        print("Hmmm....Results from Maxxie_Max3_WayOne show that the largest test subject of two is: ", Maxxie_Max3_WayOne(number_one,number_two,number_three))
    else:
        print("I want other test subjects...These ones won't do....")
    
    if Maxxie_Max3_Shortcut(number_one,number_two,number_three) == 0:
        print("Hmmm....Results from Maxxie_Max3_Shortcut show that the largest test subject of two is...: ", Maxxie_Max3_Shortcut(number_one,number_two,number_three))
    else:
        print("I want other test subjects...These ones won't do eitherrrrr....")        

if __name__ == '__main__':
    main()