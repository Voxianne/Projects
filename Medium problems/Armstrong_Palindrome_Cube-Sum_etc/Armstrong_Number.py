
#Armstrong number or Narcissistic number is a number that is equal to 
#the sum of its own digits raised to the power of the number of digits

def Armstrong_Number(number,new_number=0):
    number_of_digits = len(str(number))
    while number > 0:
        last_digit = number%10
        new_number = new_number + last_digit**number_of_digits
        number = number // 10
    return new_number

def main():
    number = int(input("Please give me a number to check wether it is an Armstrong Number or not: "))

    if Armstrong_Number(number) == number:
        print("The number is an Armstrong Number!")
    else:
        print("The number is NOT an Armstrong Number!")
    pass


if __name__=='__main__':
    main()