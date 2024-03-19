
chieucao=float(input("Nhap chieu cao cua ban : "))
cannang=float(input("Nhap can nang cua ban : "))

while (chieucao <=0 ) or (cannang <=0):
    print("Ban nhap thong tin khong hop le ! \n Moi ban nhap lai : ")
    chieucao=float(input("Nhap chieu cao cua ban : "))
    cannang=float(input("Nhap can nang cua ban : "))

BMI=cannang/(chieucao**2)
print ("Chi so BMI cua ban ", BMI)

if BMI < 16 :
    print("Gay cap do III")
elif BMI >=16 and BMI<17:
    print("Gay cap do II")
elif BMI >=17 and BMI <18.5:
    print("Gay cap do I")
elif BMI >=18.5 and BMI <25 :
    print("Binh thuong")
elif BMI <=25 and BMI<30:
    print("Thua can")
elif BMI >=30 and BMI<35 :
    print("Beo phi cap do I")
elif BMI <=35 and BMI <40:
    print("Beo phi cap do II")
else :
    print ("Beo phi cap do III")


