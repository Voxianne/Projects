def Divisible_3or5(number):
    result = []
    for i in range(1,number+1):
        if i%5 == 0 or i%3 == 0:
            result.append(i)
        else:
            continue
    if not result:
        return "None"
    else:
        return result

def Devisible_5or3_Alt(Number):
    resultalt = [x for x in range(1,Number+1) if x%5==0 or x%3==0 ]
    return resultalt
    

def main():
    number = int(input("Gimme a number to work with, pls!!: "))

    print("The results of this , according to Divisible_3or5, is: ", Divisible_3or5(number))
    print("The results of this , according to Divisible_5or3_Alt, is: ", Devisible_5or3_Alt(number))

    pass

if __name__ =='__main__':
    main()