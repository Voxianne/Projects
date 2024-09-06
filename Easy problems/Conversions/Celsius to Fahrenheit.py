def Celsius_to_Fahrenheit(celsius):
    fahrenheit = ((celsius*9)/5) + 32
    return fahrenheit


def main():
    celsius = float(input("Please gimme temperature!!: "))

    print("The result, according to the function Celsius_to_Fahrenheit: ", Celsius_to_Fahrenheit(celsius))
    pass

if __name__=='__main__':
    main()