from GCD import GCD

def LCM(number_a,number_b):
    lcm = abs(number_a*number_b)/GCD(number_a,number_b)
    return lcm

def LCM_Alt(number_a,number_b):
    list_a = [i for i in range(number_a,number_a*11+1,number_a)]
    list_b = [i for i in range(number_b,number_b*11+1,number_b)]
    for i in range(0,len(list_a)):
        for j in range(0,len(list_b)):
           if list_a[i] == list_b[j]:
                print(list_a[i],end ='')
                return None

#This solution is from Programming Hero
def Calculate_LCM(a,b):
    lcm = max(a,b) 
    #We take the largest of the two and if the remainder of at least one of the two
    #variables(lcm%a and lcm%b) is equal to zero, then return it 
    while lcm % a != 0 or lcm % b != 0:
        lcm += 1
    return lcm 

####################
#Keep in mind, you can also just import the math library and use the lcm function. Example math.lcm(a,b)
####################


def main():
    number_two_list =[]
    while 1:
        if len(number_two_list) != 2:
            number = int(input("Give me two numbers to devide: "))
            number_two_list.append(number)
        else:
            break
    print("Lowest Common Multiplier of",number_two_list[0],"and",number_two_list[1],"is:",LCM(number_two_list[0],number_two_list[1]))

    print("Lowest Common Multiplier of", number_two_list[0], "and", number_two_list[1], "is:",end = ' ') 
    LCM_Alt( number_two_list[0], number_two_list[1])

    print("\nLowest Common Multiplier of",number_two_list[0],"and",number_two_list[1],"is:",Calculate_LCM(number_two_list[0],number_two_list[1]))

    pass


if __name__=='__main__':
    main()
