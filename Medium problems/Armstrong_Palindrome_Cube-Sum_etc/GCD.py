def GCD(number1,number2,minn=0):
    for i in range(1,min(number1,number2)+1):
        if number1%i == 0 and number2%i == 0:
            minn = i
    return minn

#This solution was from Programming Hero. 
def GCD_Alt(a,b):
    if b == 0:
        print(a , end = '')
        return 0
    else:
        GCD_Alt(b, a % b)

####################
#Keep in mind, you can also just import the math library and use the gcd function. Example math.gcd(a,b)
####################

def main():
    number_two_list = []
    while 1:
        if len(number_two_list) != 2:
            number = int(input("Give me two numbers to devide: "))
            number_two_list.append(number)
        else:
            break
    print("Greatest Common Divisor of",number_two_list[0],"and",number_two_list[1],"is:",GCD(number_two_list[0],number_two_list[1]))
    print("Greatest Common Divisor of",number_two_list[0],"and",number_two_list[1],"is:",end=' ')
    GCD_Alt(number_two_list[0],number_two_list[1])


if __name__=='__main__':
    main()
