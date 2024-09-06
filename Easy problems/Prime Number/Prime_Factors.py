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
    prime_factors = []
    for i in range(len(factors)):
        if Check_Prime_Boolean(factors[i]):
            prime_factors.append(factors[i])
        else:
            continue
    print("The prime factors are: ", prime_factors )

#That's the solution from Programming Hero
def get_prime_factors(number):
    factors = []
    divisor = 2
    while number > 2:
        if number%divisor == 0:
            factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1
    prime_factors_clean = list(dict.fromkeys(factors))
    return prime_factors_clean

def main():
    upper_limit = int(input("Please give me a number: "))

    Factors(upper_limit)
    print("The prime factors for", upper_limit,"are: ", get_prime_factors(upper_limit))

if __name__ =='__main__':
    main()