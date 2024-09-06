import math

def Binary_to_Decimal(number,total = 0):
    for i in range(len(number)-1,-1,-1):
        total = total + number[i]*math.pow(2,i) # Two asterisks also mean math.pow(2,i)
    return total

def main():
    
    binary_list = []
    binary_num = input("Gimme a binary number :")

    binary_list[:] = binary_num
    for i in range(len(binary_list)):
        binary_list[i] = int(binary_list[i])
    print(Binary_to_Decimal(binary_list))
    pass

if __name__=='__main__':
    main()
