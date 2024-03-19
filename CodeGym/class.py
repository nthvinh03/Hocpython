class HCN:
    #khai báo thuộc tính và gán giá trị 
    chieu_dai=0

    chieu_rong=0

    #khai báo các phương thức 
    def dien_tich(self):
        return self.chieu_dai*self.chieu_rong
    def chu_vi(self):
        return (self.chieu_dai+self.chieu_rong)*2
    

#khai báo đối tượng 

HCM1=HCN()

HCM1.chieu_dai=100
HCM1.chieu_rong=50

S=HCM1.dien_tich()
CV=HCM1.chu_vi()

print("Dien tich cua hinh chu nhat = ",S)
print("Chu vi cua hinh chu nhat = ",CV)