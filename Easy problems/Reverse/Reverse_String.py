from audioop import reverse


def reverse_string(string):
    reverse_string =''
    for char in string:
        reverse_string = char + reverse_string
    return reverse_string



def main():
    string = input("Give me a string to play with: ")

    print("In reverse,it is: ", reverse_string(string))
    
    print("In reverse--by using a shortcut--it is: ", string[::-1])


if __name__=='__main__':
    main()
