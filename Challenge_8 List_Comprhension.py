def Permutations():
    x = int(input("Gimme number One!: "))
    y = int(input("Gimme number Two!: "))
    z = int(input("Gimme number Three!: "))

    num = int(input("Gimme a number to compare!:"))

    List_P = [(a, b, c) for a in range(x+1) for b in range(y+1)
              for c in range(z+1) if (x+y+z) != num]
    print(List_P)

if __name__=='__main__':
    Permutations()