from audioop import reverse


def Second_Smallest(number):
    number.sort(reverse=True) #it sorts the list from biggest to smallest with reverse being True. the end of the list is with [-1].Therefore, the second smallest is [-2]
    return number[-2]


def Second_Smallest_WayTwo(number):
    minnie = min(number)
    for check in range(len(number)):
        if minnie == number[check]:
            number.pop(check)
            break
    return min(number)

def Second_Smallest_WayOne(number):
    min = number[0]
    min2 = number[0]
    for check in range(len(number)):
        if min >= number[check]:
            min = number[check]
    for check in range(len(number)):
        if min == number[check]:
            continue
        elif min2 > number[check]:
            min2 = number[check]
    return min2

def main():

    str_list = input("Gimme a list of numbers with commas to seperate them!!: ")
    number_list = str_list.split(',')

    #num_list=[]
    #num_list[:] = str_list.split(',')

    for i in range(len(number_list)):
        number_list[i] = int(number_list[i])
        #num_list[i] = int(num_list[i])
    pass

    print("The second smallest is according to the function Second_Smallest is: ", Second_Smallest(number_list))
    print("The second largest ,according to function Second_Largest_WayOne, is",Second_Smallest_WayOne(number_list))
    print("The second largest ,according to function Second_Largest_WayTwo, is",Second_Smallest_WayTwo(number_list))



if __name__=='__main__':
    main()
