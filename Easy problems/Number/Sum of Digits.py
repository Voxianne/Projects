def Sum_of_Digits_WayOne(number):
    total = 0
    i = number
    while i > 0:
        num = i%10
        total = num + total
        i = i // 10
    return total

def Sum_of_Digits_Shortcuts(number, total = 0):
    if number > 0:
        return Sum_of_Digits_Shortcuts(number = number//10, total = number%10 + total )
    else:
        return total
    pass



def main():
    number = int(input("GimmeGimme num num! :"))

    print("The sum of all the digits smaller or equal to", number,",according to Sum_of_Digits_WayOne, is ", Sum_of_Digits_WayOne(number))
    print("The sum of all the digits smaller or equal to", number,",according to Sum_of_Digits_Shortcut, is ", Sum_of_Digits_Shortcuts(number))

    pass


if __name__ =='__main__':
    main()