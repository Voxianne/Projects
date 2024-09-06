from audioop import reverse


def Reverse_String_Recursive(string):
    if len(string) == 0:
        return string
    else:
        return Reverse_String_Recursive(string[1:]) + string[0]

        
    pass

def main():

  string = input("Give me a string to play with: ")

  print(Reverse_String_Recursive(string))
  print("")


if __name__=='__main__':
    main()