from audioop import reverse
from Check_Prime import Check_Prime_Boolean

def Factors(number):
    factors = []
    for i in range(1,number):
        if number%i == 0:
            factors.append(i)
        else:
            continue
    Prime_Factors(factors)

def Prime_Factors(factors):
    for i in range(len(factors)):
        if Check_Prime_Boolean(factors[i]):   
            print("The smallest prime factor is: ", factors[i] )
            break
        else: 
            continue

#That's the solution from Programming Hero
def get_prime_factors(number):
    divisor = 2
    while number > 2:
        if number%divisor == 0:
            break
        else:
            divisor += 1
    return divisor


def main():
    upper_limit = int(input("Please give me a number: "))

    Factors(upper_limit)
    print("The smallest prime factor for", upper_limit,"are: ", get_prime_factors(upper_limit))

if __name__ =='__main__':
    main()