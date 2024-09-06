
def Rem_Duplicates(string):
    #Since dictionaries dont have duplicates, it erases any of them, by counting on the list string and then makes it again into a list
    string = list(dict.fromkeys(string))
    return string

def Remove_Duplicates(string):
    
    for char in range(len(string)):
        for i in range(len(string)):
            if string[char] == string[i] and char != i:
                string[i] = ''
    string = [string[char] for char in range(len(string)) if string[char] != '']             
    return string

def Remove_Duplicates_Alt(string):
    result = ''
    for char in range(len(string)):
        if string[char] not in result:
            result += string[char]
    string_list=[]
    string_list[:] = result
    return string_list

def main():

    string_list = []
    string = input("Give me any string!And i shall remove all fakers!: ")
    string_list[:] = string

    print(Rem_Duplicates(string_list))
    print(Remove_Duplicates(string_list))
    print(Remove_Duplicates_Alt(string_list))


if __name__=='__main__':
    main()
