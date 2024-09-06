from cmath import sqrt


import math

def Triangle_Area(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The triangle area is:", round(area,2))

def main():

    a_side = float(input("Give me the a side of the triangle: "))
    b_side = float(input("Give me the b side of the triangle: "))
    c_side = float(input("Give me the c side of the triangle: "))

    Triangle_Area(a_side,b_side,c_side)


if __name__=='__main__':
    main()