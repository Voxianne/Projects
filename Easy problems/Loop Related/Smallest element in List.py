
def Small_Num_List_WayOne(number,i):
    for check in range(len(number)):
        i = min(i,number[check])
    return i

def Small_Num_List_WayTwo(number):
    minnie = number[0]
    for check in range(len(number)):
        if number[check] <= minnie:
            minnie = number[check]
    return minnie

def Small_Num_List_WayThree(number):
    return min(number)

def Small_Num_List_Shortcut(number):
    number.sort(reverse = False)
    return number[0]

def main():

    str_list = input("Gimme list with whitespaces between! :")
    num_list = str_list.split(' ')

    for i in range(len(num_list)):
        num_list [i] = int(num_list[i])

    print("The smallest number from the given list,according to the function Small_Num_List_WayOne, is ",Small_Num_List_WayOne(num_list,num_list[0]))
    print("The smallest number from the given list,according to the function Small_Num_List_WayTwo, is ",Small_Num_List_WayTwo(num_list))
    print("The smallest number from the given list,according to the function Small_Num_List_WayThree, is ",Small_Num_List_WayThree(num_list))
    print("The smallest number from the given list,according to the function Small_Num_List_Shortcut, is ",Small_Num_List_Shortcut(num_list))

if __name__=='__main__':
    main()
