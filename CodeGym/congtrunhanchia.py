#cong
def cong(a:float ,b:float):
    return a+b
#tru
def tru(a:float ,b:float):
    return a-b
#nhan
def nhan(a:float ,b:float):
    return a*b
#chia
def chia(a:float ,b:float):
    return a/b

index1=float(input("Nhap so thu nhat : "))
index2=float(input("Nhap so thu hai "))
choose=input("Nhap dau phep tinh : ")

if choose=="+":
    print("Ket qua phep cong : {0} + {1} = {2}".format(index1,index2,cong(index1,index2)))
elif choose=="-":
    print("Ket qua phep tru : {0} - {1} = {2}".format(index1,index2,tru(index1,index2)))
elif choose=="*":
    print("Ket qua phep nhan : {0} * {1} = {2}".format(index1,index2,nhan(index1,index2)))
elif choose==":":
    print("Ket qua phep chia : {0} : {1} = {2}".format(index1,index2,chia(index1,index2)))
else :
    print("Error !")