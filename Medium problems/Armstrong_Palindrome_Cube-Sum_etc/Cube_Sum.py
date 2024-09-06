def Cube_Sum(number,total = 0):
    if number != 0:
        return Cube_Sum(number-1,total=total + number**3)
    else:
        print(total, end =' ')


def Cube_Sum_Alt(number):
   return (number*(number+1)/2)**2 #formula  to calculate the sum of cubes

def main():
    while 1:
        number_base = float(input("Give me an interger :"))
        if not number_base.is_integer():
            continue
        else:
            break
    print('The result of the cube sum is:',end=' ') #new='' allows multiple prints to be in the same line
    Cube_Sum(number_base)
    print('')

    print('The result of the cube sum is:',Cube_Sum_Alt(number_base)) #new='' allows multiple prints to be in the same line


if __name__=='__main__':
    main()
