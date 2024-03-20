def  min_max():
    lst=[]
    n=int(input("Nhập số phần tử của mảng : "))
    for i in range (0,n):
        enter_number=int(input("Phần tử [{0}] = ".format(i)))
        lst.append(int(enter_number))
    
    for i in lst:
        print(i,end=" ")

    min=lst[0]
    max=lst[0]
    for i in lst:
        if min > i:
            min=i

    return min

print("\nMin ",min_max())