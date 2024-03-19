gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00,
           "Television", 1000, "Laptop Case", "Camera Lens"]

lst_char=[]
lst_number=[]

for i in gadgets:
    if isinstance(i,str):
        lst_char.append(i)
    else:
        lst_number.append(i)

print("List chua chuoi : ",lst_char)
print("\nList chua so ",lst_number)

#sap xep theo abc
lst_char.sort()
print(lst_char)
lst_char.sort(reverse=True)
print("\n",lst_char)

lst_number.sort()
print("\n",lst_number)
lst_number.sort(reverse=True)
print("\n",lst_number)