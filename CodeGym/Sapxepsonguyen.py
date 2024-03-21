def sapxep(num1,num2,num3):
    temp=0
    if num2<num1 and num2<num3:
        temp=num1
        num1=num2
        num2=temp
    elif num3<num1 and num3<num2:
        temp=num1
        num1=num3
        num3=temp

    if num3<num2:
        temp=num2
        num2=num3
        num3=temp
    
    return num1,num2,num3

x=int(input("Enter your first number : "))
y=int(input("Enter your second number : "))
z=int(input("Enter your third number : "))

print("Original number : ",x,y,z)
a,b,c=sapxep(x,y,z)
print("Sorted number : ",a,b,c)