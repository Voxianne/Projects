def Gravitational_Force(m1,m2,r,g):
    print("The Gravitational Force of those is:", (m1*m2*g)/r**2)


def main():
    g = 6.673*(10**(-11))

    m1 = float(input("Please give me the mass of the first object: "))
    m2 = float(input("Please give me the mass of the second object: "))
    distance = float(input("Please give me the distance between the two objects: "))

    Gravitational_Force(m1,m2,distance,g)


if __name__=='__main__':
    main()
