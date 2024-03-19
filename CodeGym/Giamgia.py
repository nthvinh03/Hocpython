index=input("Enter your money : ")
indexx=int(index)

if indexx <75:
    indexx==indexx
elif indexx >=75 and indexx <100:
    indexx-=15
elif indexx >=100 and indexx <150:
    indexx-=25
else :
    indexx-=50

print("Amount : ",indexx)