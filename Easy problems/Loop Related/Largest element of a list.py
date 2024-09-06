def Large_Num_List_WayOne(number,i):
    for check in range(0,len(number)):
        i = max(i,number[check])
    return i

def Large_Num_List_WayTwo(number):
    max_num  = number[0]
    for check in range(0,len(number)):
        if number[check] >= max_num:
            max_num = number[check]
    return max_num


def Large_Num_List_WayThree(number):
    return max(number)


def Large_Num_List_Shortcut(number):
    number.sort(reverse = True)
    return number[0]
    


def main():
    
    str_list = input("Gimme a list of numbers with commas to seperate them!!: ")

    number_list = str_list.split(',')

    for i in range(0,len(number_list)):
        number_list[i] = int(number_list[i])
    
    
    print("The largest number from the given list,according to the function Large_Num_List_WayOne, is ",Large_Num_List_WayOne(number_list,number_list[0]))
    print("The largest number from the given list,according to the function Large_Num_List_WayTwo, is ",Large_Num_List_WayTwo(number_list))
    print("The largest number from the given list,according to the function Large_Num_List_WayTwo, is ",Large_Num_List_WayThree(number_list))
    print("The largest number from the given list,according to the function Large_Num_List_Shortcut, is ",Large_Num_List_Shortcut(number_list))


if __name__=='__main__':
    main()
