def Second_Largest(number):
    number.sort(reverse = True)
    return number[1]

def Second_Largest_WayOne(number):
    maxxie = max(number)
    for check in range(len(number)):
        if maxxie == number[check]:
            number.pop(check)
            break
    return max(number)

def Second_Largest_WayTwo(number):
    max = number[0]
    max2 = number[0]
    for check in range(len(number)):
        if number[check] >= max:
            max = number[check]
        elif number[check] >=max2 and number[check] < max:
            max2 = number[check]
    return max2

def main():
    
    str_list = input("Gimme a list of numbers with commas to seperate them!!: ")
    number_list = str_list.split(',')

    for i in range(0,len(number_list)):
        number_list[i] = int(number_list[i])
    print("The second largest ,according to function Second_Largest, is",Second_Largest(number_list))
    print("The second largest ,according to function Second_Largest_WayOne, is", Second_Largest_WayOne(number_list))
    print("The second largest ,according to function Second_Largest_WayTwo, is", Second_Largest_WayTwo(number_list))


    

if __name__=='__main__':
    main()
