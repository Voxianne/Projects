def Sum_of_Digits_WayOne(number):
    total = 0
    i = 0
    while i <= number:
        total = i + total
        i +=1
    return total
    
def Sum_of_Digits_WayTwo(number):
    total = 0
    for i in range(1,number+1):
        total = i + total
    return total

def Sum_of_Digits_Shortcut(number,total = 0):
    if number <= 0:
        return total
    else:
        return Sum_of_Digits_Shortcut(number-1,total=total+number)


def main():
    number = int(input("GimmeGimme num num! :"))

    print("The sum of all the digits smaller or equal to", number,",according to Sum_of_Digits_WayOne, is ", Sum_of_Digits_WayOne(number))
    print("The sum of all the digits smaller or equal to", number,",according to Sum_of_Digits_WayTwo, is ", Sum_of_Digits_WayTwo(number))
    print("The sum of all the digits smaller or equal to", number,",according to Sum_of_Digits_Shortcut, is ", Sum_of_Digits_Shortcut(number))

    pass


if __name__ =='__main__':
    main()