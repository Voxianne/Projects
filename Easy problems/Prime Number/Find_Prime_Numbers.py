from Check_Prime import Check_Prime_Boolean

def Prime_Numbers(number):
    prime_numbers = []
    for i in range(0,number+1):
        check = i
        if not Check_Prime_Boolean(check):
            continue
        else:
            prime_numbers.append(i)
    #prime_numbers_clean = list(dict.fromkeys(prime_numbers))
    print("The prime numbers from 1 to",number," are :", prime_numbers)


    pass
def main():

    number = int(input("Please give me anumber to work with: "))

    Prime_Numbers(number)
    pass

if __name__=='__main__':
    main()
