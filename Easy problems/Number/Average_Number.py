def Average_Number_WayOne(number):
    result = 0
    for i in range(0,len(number)): 
        result=result + number[i]
    length = len(number)  
    return result / length

def Average_Number_Shortcut(number):  
    return sum(number) / len(number)

def main():
    number = []
    i = 1
    while i != 0.1:
        i = float(input("Please put a number in the list except 0.1: "))
        number.append(i)
    print("The result from Average_Number_WayOne is: ",Average_Number_WayOne(number))
    print("The result from Average_Number_Shortcut is: ",round(Average_Number_Shortcut(number),2)) #round stroggilopoiei ton arithmo kata 2,3,4 etc dekadika 


if __name__=='__main__':
    main()