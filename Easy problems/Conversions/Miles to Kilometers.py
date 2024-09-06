def Miles_to_Kilometers(miles):
    kilometers = miles*1.609344
    return kilometers

def Miles_to_Kilometers_Alt(miles):
    kilometers = miles*1 + miles*0.6
    return kilometers

def main():

    miles = float(input("Gimme miles to convert to kilometers!: "))

    print("According to the function Miles_to_Kilometers," ,miles, "equal to:", Miles_to_Kilometers(miles),"kilometers! ")
    print("According to the function Miles_to_Kilometers," ,miles, "equal to:", Miles_to_Kilometers_Alt(miles),"kilometers! ")
    print("The second is not quite as accurate as the first one but it is close!")

    pass

if __name__=='__main__':
    main()