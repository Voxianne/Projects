def Decimal_to_Binary_Recursive(Quotient,result=''):
    if Quotient == 0:
        return result[::-1] #strings can also be treated as lists without needing to be a list with [::-1]
    else:
        return Decimal_to_Binary_Recursive(Quotient//2,result = result + str(Quotient%2))

def Decimal_to_Binary_Recursive_Alt(Quotient): #This finction was from Pragramming Hero App. Check it out carefully!
    if Quotient > 1:
        Decimal_to_Binary_Recursive_Alt(Quotient//2)
     #The purpose of end = is to show the result in one same line, else each output will be displayed in a new line
    print(Quotient % 2, end='')

def main():

    decimal_num = int(input("Gimme a decimal number :"))

    Decimal_to_Binary_Recursive_Alt(decimal_num)
    print(" ") # This print is connected with the function Decimal_to_Binary_Recursive_Alt
    print(Decimal_to_Binary_Recursive(decimal_num))
    pass

if __name__=='__main__':
    main()
