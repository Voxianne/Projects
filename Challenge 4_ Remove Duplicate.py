def Originals(item):

    Originals = []
    for nums in item:
        if nums not in Originals:
            Originals.append(nums)
        else:
            continue
    return Originals

numbers = [7,12,200,1,2,12,7,45,3,21]
print(Originals(numbers))

#Keep in mind  in the if and to focus on what exactly the problem wants. Is it referring to numbers or string, etc