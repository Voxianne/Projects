import random

def Random_Generator():
    return random.randint(1,10)
 
def main():
    score = 0
    while 1:
        number = input("Please give me a number from 1 to 10. Else type q or Q, if you wish to quit: ")
        if number == 'q' or number == 'Q':
            print("Aww,leaving so soon? Please come back soon!")
            break
        elif number.isdigit():
            if int(number) > 0 and int(number) <= 10:
                 if int(number) == Random_Generator():
                    print("We got a winner,folks!")
                    score += 10
                    print("Le score now is:", score)
                 else:
                     print("Sorry, but the correct answer is", Random_Generator())

    pass

if __name__=='__main__':
    main()
