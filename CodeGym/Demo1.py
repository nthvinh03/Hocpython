n=int(input("Rong = "))
m=int(input("Dai= "))

for i in range(1,n):
    for j in range (1,m):  
        if i==1 and i==n-1:
            print(" * ",end=" ")
        else :
            if j==1 and j==m-1:
                print(" * ")
            else:
                print(" ")
    print("\n")
  