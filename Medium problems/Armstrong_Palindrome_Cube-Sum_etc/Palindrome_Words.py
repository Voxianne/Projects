def Palindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False

def main():
    string = input("Give me a string to check wether it is palindrome or not! : ")

    if Palindrome(string):
        print(string ,"is palindrome!")
    else:
        print(string, "is not palindrome!")
    pass

if __name__=='__main__':
    main()