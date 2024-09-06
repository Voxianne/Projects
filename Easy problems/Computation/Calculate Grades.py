def Calculate_Average_Grade(grades):
    average = sum(grades)/len(grades)
    if average >= 18:
        print("The student got an A with:" , average)
    elif average >=15:
        print("The student got a B with: " , average)
    elif average >=13:
        print("The student got a C with: ", average)
    elif average >= 10:
        print("The student got a D with:", average)
    else:
        print("The student got an F with:", average)


def main():

    while 1:
        grade = input("What grades do you want to put? Please insert them with commas (The max grade is 20, subjects must be 5) : ")
        grade = grade.split(',')
        if len(grade) != 5:
            continue
        else:
            break

    grades_float = []
    grades_float[:] = grade

    for i in range(len(grades_float)):
        grades_float[i] = float(grades_float[i])
        while 1:
            if float(grades_float[i]) > 20:
                print("Grade:", grades_float[i])
                grades_float[i] = float(input("Please correct the grade as it is higher than 20: "))
            elif float(grades_float[i]) < 0:
                print("Grade:", grades_float[i])
                grades_float[i] = float(input("Please enter a grade between 0 and 20: "))
            else:
                break
    Calculate_Average_Grade(grades_float)

if __name__=='__main__':
    main()
