from cmath import e
import math

def Compound_Interest(Principal_Amount,Month_Year,Interest_Rate,Duration):
    #Converting Interest_rate in decimal
    r = Interest_Rate / 100
    if Month_Year == 0:
        A = round(Principal_Amount*(e**(r*Duration)),2)
        I = round(A - Principal_Amount,2)
    else:
        A = round(Principal_Amount*(1 +r/Month_Year)**(Month_Year*Duration),2)
        I = round(A - Principal_Amount,2)
    return I

def main():
    Principal_Amount = float(input("How much money did you borrow? :"))
    Interest_annual_rate =  float(input("How much interest rate? :"))
    Duration = float(input("For how long? :"))

    print(" -> 0 (Continuously) \n -> 365 or 360(Daily) \n -> 52(Weekly) \n -> 26 (Bi-Weekly) \n -> 24 (Semi-Monthly) \n -> 12 (Monthly) \n -> 6 (Bi-Monthly) \n -> 4 (Quarterly) \n -> 2 (Semi-Annually) \n -> 1 (Annually)" )
    Month_Year= int(input("How many times per year? Please choose one of the above :"))
   
    while 1:
        if Month_Year == 0:
            print("The compound interest Continuously is: ", Compound_Interest(Principal_Amount,Month_Year,Interest_annual_rate,Duration))
            break
        elif Month_Year == 365 or Month_Year == 360:
            print("The compound interest Daily is: ", Compound_Interest(Principal_Amount, Month_Year, Interest_annual_rate,Duration))
            break
        elif Month_Year == 52:
            print("The compound interest Weekly is: ", Compound_Interest(Principal_Amount,Month_Year,Interest_annual_rate,Duration))
            break
        elif Month_Year == 26:
            print("The compound interest Bi-Weekly is: ", Compound_Interest(Principal_Amount,Month_Year,Interest_annual_rate,Duration))
            break
        elif Month_Year == 24:
            print("The compound interest Semi-Monthly is: ", Compound_Interest(Principal_Amount,Month_Year,Interest_annual_rate,Duration))
            break
        elif Month_Year == 12:
            print("The compound interest Monthly is: ", Compound_Interest(Principal_Amount,Month_Year,Interest_annual_rate,Duration))
            break
        elif Month_Year == 6:
            print("The compound interest Bi-Monthly is: ", Compound_Interest(Principal_Amount,Month_Year,Interest_annual_rate,Duration))
            break
        elif Month_Year == 4:
            print("The compound interest Quarterly is: ", Compound_Interest(Principal_Amount,Month_Year,Interest_annual_rate,Duration))
            break
        elif Month_Year == 2:
            print("The compound interest Semi-Annually is: ", Compound_Interest(Principal_Amount,Month_Year,Interest_annual_rate,Duration))
            break
        elif Month_Year == 1:
            print("The compound interest Annually is: ", Compound_Interest(Principal_Amount,Month_Year,Interest_annual_rate,Duration))
            break
        else:
            print(" -> 0 (Continuously) \n -> 365 or 360(Daily) \n -> 52(Weekly) \n -> 26 (Bi-Weekly) \n -> 24 (Semi-Monthly) \n -> 12 (Monthly) \n -> 6 (Bi-Monthly) \n -> 4 (Quarterly) \n -> 2 (Semi-Annually) \n -> 1 (Annually)" )
            Month_Year= int(input("How many times per year? Please choose one of the above: "))


if __name__=='__main__':
    main()
