import math

def Floor_Division_WayOne(number_up,number_down):
    result = int(number_up / number_down)
    return result
def Floor_Division_WayTwo(number_up, number_down):
    result = number_up // number_down            #The two slashes means the interger part of the division as well. Its more like a shortcut
    return result

def Floor_Division_Shortcut(number_up,number_down):
    return math.floor(number_up/number_down)     #the math.floor() takes only ONE argument! CAREFUL GURL!

def main():
    number_up = int(input("Give me the numerator thats up to execution!: "))
    number_down = int(input("Give me the unnamed/executor!: "))

    print("The result of the function Floor_Division_WayOne is:", Floor_Division_WayOne(number_up,number_down))
    print("The result of the function Floor_Division_WayTwo is:", Floor_Division_WayTwo(number_up,number_down))
    print("The result of the function Floor_Division_Shortcut is:", Floor_Division_Shortcut(number_up,number_down))


if __name__=='__main__':
    main()
