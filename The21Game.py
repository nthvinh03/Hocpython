import random as r 



while True:
    current_number=0
    #khoi tao bien nguoi choi 1 :human 0:computer
    current_player=r.randint(0,1)
    if current_player==1:
        current_player="Human"
    else :
        current_player=="Computer"
    
    while current_number<=21:
        print(current_number)
        if current_player ==1:
            lst_choice=['1','2','3']
            player_choice=input("Nhap vao gia tri cua nguoi choi : ")
            while player_choice not in lst_choice:
                print("Gia tri nhap chua dung !\n Moi nhap lai gia tri .")
                player_choice=input("Nhap vao gia tri : ")
            player_choice1=int(player_choice)
            current_number+=player_choice1
            print("Diem so : ",current_number)
            if current_number>=21:
                print("Nguoi choi thua , may da thang  , diem so da la 21",current_number)
                break
            else:
                current_player=0
        else :
            computer_choice=" "
            print("Nhap vao gia tri cua may : ")
            computer_choice=r.randint(1,3)
            computer_choice1=int(computer_choice)
            current_number+=computer_choice1
            print("Diem so : ",current_number)
            if current_number>=21:
                print("Ban da thang , may da thua, diem so da la 21 ",current_number)
                break
            else:
                current_player=1
    play_again=int(input("Ban co muon choi lai khong (1:Yes / 2:No) : "))
    if play_again ==1:
        continue
    else:
        break


            

