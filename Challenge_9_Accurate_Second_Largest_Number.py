if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

 
    arr.sort(reverse = True)
    print(arr) 
    maxx = max(arr)
    for i in range(len(arr)):
        if maxx != arr[i]:
            print(arr[i])
            break
    