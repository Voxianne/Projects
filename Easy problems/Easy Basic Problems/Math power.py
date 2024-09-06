import math

def Power_Up_WayOne(num_one, num_power):
    total = 1
    for i in range(num_power):
        total = total*num_one
    return total

def Power_Up_WayTwo(num_one,num_power):
    return num_one**num_power          #Two asterisks mean x up in the power of y 

def Power_Up_Shortcut(num_one,num_power):
    return math.pow(num_one,num_power)

def main():
    num_one = int(input("Gimme the number you want as interger!: "))
    num_power = int(input("Gimme the number you will use for the MATH POWAH! : "))

    print("The funtion Power_Up_WayOne has a result of: ", Power_Up_WayOne(num_one,num_power))
    print("The funtion Power_Up_WayTwo has a result of: ", Power_Up_WayTwo(num_one,num_power))
    print("The funtion Power_Up_Shortcut has a result of: ", Power_Up_Shortcut(num_one,num_power))

if __name__ == '__main__':
    main()