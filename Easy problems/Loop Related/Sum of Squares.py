import math

def Sum_of_Squares_WayOne(num,total=0):
    for i in range(num+1):
        total = total + math.pow(i,2) # Here even the two asterisks would also suffice since that also means math.pow()
    return total


def Sum_of_Squares_WayTwo(num):
   sum = num*(num+1)*(2*num+1)/6 #Its a formula that helps you get the sum of squares easier, in one line!
   return sum

def Sum_of_Squares_Shortcut(num,total = 0):
    if num < 0:
        return total
    else:
        return Sum_of_Squares_Shortcut(num-1,total = total + math.pow(num,2))

def main():

    num = int(input("Gimme a num to play with!!: "))

    print("The results from the function Sum_of_Squares_WayOne is: ", Sum_of_Squares_WayOne(num))
    print("The results from the function Sum_of_Squares_WayOne is: ", Sum_of_Squares_WayTwo(num))
    print("The results from the function Sum_of_Squares_Shortcut is: ", Sum_of_Squares_Shortcut(num))

    pass

if __name__=='__main__':
    main()
