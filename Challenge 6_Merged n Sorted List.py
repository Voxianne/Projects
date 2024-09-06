  
def combine_lists(Lista,Listb):
    Merged_List = Lista + Listb
    Merged_List.sort()
    
    return Merged_List


def main():

    List_1 = [4,6,2,3,1,10]
    List_2 = [5,8,11,0,34]
    print(combine_lists(List_1,List_2))

if __name__ == '__main__':
    main()
