

from enum import Flag


def Check_Prime(number):
    check = 1
    for i in range(2,number+1):
        if number%i==0:
            check+=1
    if check != 2:
        print(number ,"is not a prime number.")
    else:
        print(number ,"is a prime number.")


def Check_Prime_Alt(number):
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a prime number.")
            break
        else:
            print(number, "is a prime number.")

def Check_Prime_Boolean(number):

    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
            

def main():
    check_number = int(input("Give me an interger to work with: "))

    Check_Prime(check_number)
    Check_Prime_Alt(check_number)
    if not Check_Prime_Boolean(check_number):
        print(check_number, "is not a prime number.")
    else:
        print(check_number, "is a prime number.")

if __name__ =='__main__':
    main()
