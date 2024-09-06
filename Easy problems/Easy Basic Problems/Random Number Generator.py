from random import randint, random


import random

def Random_Generator(num_limit):
    return random.randint(0,num_limit)

def main():
    num_limit = int(input("Give me a limit!: "))

    print("Le random generator shall give you the numberrrr: ", Random_Generator(num_limit))

if __name__=='__main__':
    main()