def Sum_List(number):
    return sum(number)

def main():
    i = False
    if not i:

        limit = int(input("How many nums nums?? :"))
        number = []
        while not i:
            num =  int(input("Gimme Gimme num num!! :"))
            number.append(num)
            if limit > 1:
                limit -=1
            else:
                i = True 
        print("Le sum of da elementals izzz: " ,Sum_List(number))         

    if i:
        number_alt = []
        num_alt = input("Give me the numbers alltogether nouw! :")
        number_alt[:] = num_alt #Use this to turn a string into a list of elements!
        for i in range(0,len(number_alt)):
            number_alt[i] = int(number_alt[i])
        print("Le sum of da elementals,thenkz to the converzionnn, izzz: " ,Sum_List(number_alt))      




if __name__=='__main__':
    main()