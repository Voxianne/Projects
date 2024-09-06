def Multiply (first_num,second_num):
    return "Result would be ",first_num*second_num

def main():
    first_num = int(input("Give me number one as interger: "))
    second_num = float(input("Give me number two as float: "))
    print(Multiply(first_num,second_num))

if __name__=='__main__':
    main()