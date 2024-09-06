from audioop import reverse


def Reverse_String_with_Stack(string):
    reverse_string = ''
    reverse_list = []
    for char in string:
        reverse_list.append(char)
    while reverse_list:
        reverse_string = reverse_string + reverse_list[-1]
        reverse_list.pop()
    return reverse_string


def main():

    string = input("Give me a string to play with: ")

    print("In reverse, it is:",Reverse_String_with_Stack(string))
    pass

if __name__=='__main__':
    main()