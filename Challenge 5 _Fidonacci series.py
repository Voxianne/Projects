
def Fidonacci_Series(num):
    List = [0,1]
    for i in range(1,num):
        item = List[-1] + List[-2]
        List.append(item)
    return List


def main():

    print(Fidonacci_Series(9))

if __name__ == '__main__':
    main()