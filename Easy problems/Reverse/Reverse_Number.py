def Reverse_Number(number):
    reverse_number = ''
    while number>0:
        last_digit = int(number%10)
        reverse_number = reverse_number + str(last_digit)
        number = number//10
    return reverse_number

def Reverse_Number_Recursive(number):
    if len(number) == 0:
        return number
    else:
        return Reverse_Number_Recursive((number[1:])) + str(number[0])


def Reverse_Number_WayTwo(number):
    reverse_number = 0
    while number>0:
        last_digit = int(number % 10)
        reverse_number = reverse_number*10 + last_digit
        number = number//10
    return reverse_number

def main():
    number = int(input("Give me a number to play with: "))

    print(Reverse_Number(number))
    print(Reverse_Number_Recursive(str(number)))
    print(Reverse_Number_WayTwo(number))
    pass

if __name__=='__main__':
    main()
