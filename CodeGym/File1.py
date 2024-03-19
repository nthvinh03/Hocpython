
#Mở file ở chế độ đọc ghi
file=open("CodeGym/data.txt","r+")
#print("Tên của file là ",file.name)
#print("file có đóng hoặc không ",file.closed)
#print("chế độ mở file ",file.mode)
file.write("\nPython la ngon ngu tot nhat")



line1=file.readline()
line2=file.readline()
line3=file.readline()



print("Dong 1 ",line1)
print("Dong 2 ",line2)
print("Dong 2 ",line3)

file.close()






#Mở file chỉ để độc r
#Mở file để độc và ghi r+
#Mở file trong chế độ đọc cho định dạng nhị phân ,đây là chế độ mặc định ,con trỏ tại phần bắt đầu của file rb
#Mở file để đọc và ghi trong định dạng nhị phân. con trỏ tại phần bắt đầu của file rb+
#Tạo một file mới để ghi nếu file đã tồn tại thì ghi file mới w
#Tạo một file mới để đọc và ghi nếu file đã tồn tại thì ghi file mới w+

