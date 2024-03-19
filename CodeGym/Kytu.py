char=input("Input your char : ")
width=int(input("Width : "))
height=int(input("Height : "))

for i in range ( 1,height+1):
    print_char=""
    for j in range(1,width+1):
        if i ==1 or i == height:
            print_char+=char
        else :
            if j==1 or j==width:
                print_char+=char
            else:
                print_char+=" "
    print(print_char)