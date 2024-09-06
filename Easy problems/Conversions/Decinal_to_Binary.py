def Decimal_to_Binary(Quotient):
    binary = ''
    while 1:
        left = int(Quotient % 2)
        #Here, it could also be used binary += str(Quotient%2)
        Quotient = int(Quotient / 2)
        binary += str(left)
        if Quotient == 0:
            break
    binary_list = []
    binary_list[:] = binary
    for i in range(len(binary_list)):
        binary_list[i] = int(binary_list[i])
    return binary_list[::-1]




def main():

    decimal_num = int(input("Gimme a decimal number :"))

    print(Decimal_to_Binary(decimal_num))
    pass

if __name__=='__main__':
    main()