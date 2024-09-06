
def Multiplication(number):
    i = 0
    for i in range(0,int(number)+1):
        multiply = i * int(number)
        i = i + 1
        print('',i-1,' times ', number ,' equals ', multiply)

def main():

  Num = int(input('Gimme Num! :'))

  print(Multiplication(Num))

  num1 = input('')
  num2 = input('')
  print(num1 + num2)

  
if __name__ == '__main__':
  main()
  
#def Multiplication(number):
#    Mult_Res = []
#    i = 0
#    while i <= int(number):
#        multiply = i * int(number)
#        i = i + 1
#       Mult_Res.append(multiply)
#    return Mult_Res

