import random
while True:
    choose=input("Lua chon cua ban : ")
    if choose.lower()=='q':
        print("Thoat chuong trinh")
        break
    AI=['Keo','Bua','La']
    May=random.choice(AI)
    print("Lua chon cua may : ",May)
    if(choose==May):
        print("Hoa")
    elif(choose=="Keo" and May=="Bua"):
        print("AI thang")
    elif(choose=="Bua" and May=="Keo"):
        print("Ban thang")
    elif(choose=="La" and May=="Bua"):
        print ("Ban thang")
    elif(choose=="Bua" and May=="La"):
        print("AI thang")
    elif(choose=="Keo" and May=="La"):
        print("Ban thang")
    else:
        print("AI thang")