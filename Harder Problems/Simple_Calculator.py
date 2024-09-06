import math
import os

###################################
#Checks the operator and does the necessary calculations
###################################
def Calculator(x,y,operator):   
    if operator == '+':
        return x+y
    elif operator == '-':
        return x - y
    elif operator == '/':
        return x/y
    elif operator == '*':
        return x*y
    elif operator == '//':
        return x//y
    elif operator == '%':
        return x%y
    elif operator == '**':
        return x**y
    elif operator == 'sqrt':
        return math.sqrt(x)
    
###################################
#Clears the console after each input
###################################
def ClearConsole():
        command = 'cls'
        os.system(command)


def main():

        ClearConsole()
        print("Please press C to clear all or O to quit.")
        number_1= input("")
        ClearConsole()
        ###################################
        #After getting the first input, start an infinite loop
        ###################################
        while 1:
            ###################################
            #Checks if number is a number and if not, re-input else if it is O then exit
            #else if it is C , clears it
            #Asks for Operator
            ###################################
            if str(number_1).replace('.','',1).isdigit():
                    print("Please enter what you want to do(+,-,/,//,*,**,%,sqrt) :")
                    Operator = input("")
                    ClearConsole()
                    ###################################
                    #Checks if operator is in a list else print error
                    ###################################
                    if Operator in ['+','-','/','//','*','**','%','sqrt','C','c','O','o']:
                        while 1:
                            ###################################
                            #If Operator is within the list then ask for number_2
                            ###################################
                            if Operator in ['+','-','/','*','**','//','%']:
                                number_2 = input("")
                                ClearConsole()
                                ###################################
                                #If number_2 is float, then Calculate
                                #then break to check the new number_1 and continue the loop
                                ###################################
                                if str(number_2).replace('.', '', 1).isdigit():
                                    print(number_1 , Operator, number_2, "= ",end=' ' )
                                    number_1 = Calculator(float(number_1),float(number_2),Operator)
                                    number_1 = round(number_1,2)
                                    print(number_1)
                                    break
                                elif str(number_2).upper() == 'C':
                                    number_1 = input("")
                                    break
                                elif str(number_2).upper() == 'O':
                                    number_1 = 'O'
                                    break
                                else:
                                    print("Wrong Input! Type Error: It is not float")
                            ###################################
                            #If Operator is equal to C, new input in number_1
                            #empty Operator and break, to prevent infinite loop
                            ###################################
                            elif Operator == 'sqrt':
                                number_1 = Calculator(float(number_1),0,Operator)
                                number_1 = round(number_1,2)
                                print(number_1)
                                break
                            ###################################
                            #If Operator is equal to C, new input in number_1
                            #empty Operator and break, to prevent infinite loop
                            ###################################
                            elif Operator.upper() == 'C':
                                number_1 = input(" ")
                                Operator = ''
                                ClearConsole()
                                break
                            ###################################
                            #If Operator is equal to O, change number_1's value to 'O'
                            #and break
                            ###################################
                            elif Operator.upper() == 'O':
                                number_1 = 'O'
                                break
                    else:
                        print("Wrong Input: ", Operator," is not a valid Operator!")

            ###################################
            #In case number_1 is not number then if it is O, exit
            #If it is C, ask for a new input
            #Else again input
            ###################################
            elif str(number_1).upper() == 'O':
                    print("Calculator.exe stopped working...")
                    quit()
            elif str(number_1).upper() == "C":
                number_1 = input("")
                ClearConsole()
            else:
                print("Wrong Input! Type Error: It is not float")
                number_1 = input("")
                ClearConsole()

                


if __name__=='__main__':
    main()
