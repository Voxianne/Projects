def Simple_Interest_per_Year(Principle_Amount, Percentage_Interest,Years):
    #Convert interest rate in decimal
    r = Percentage_Interest/100
    #Principal amount =  Total_Amount / (1 + r*Years) --> Total_Amount = Principal Amount(1 + r*Years/Months)
    A = round(Principle_Amount*(1 + r*Years),2)
    I = A - Principle_Amount
    return I

def main():
    Principle_Amount = float(input("How much money did you borrow, sire/ma'am? :"))
    Interest_per_year = float(input("How much interest? :"))
    Years = int(input("How many years? :"))

    print("The simple interest is: ",Simple_Interest_per_Year(Principle_Amount,Interest_per_year,Years))
    pass

if __name__=='__main__':
    main()