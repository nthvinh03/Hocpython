Thong_tin={
    "Ten":"Ninh Thanh Vinh",
    "Tuoi":"21",
    "Can_nang":"60kg"
}

#in
print(Thong_tin['Ten'])

#lay
print(Thong_tin.get("Tuoi"))


#update

Thong_tin.update({"Dia_chi":"Dao My ,Lang Giang ,Bac Giang"})


print(Thong_tin["Dia_chi"])

#xoa

Thong_tin.pop("Tuoi")

print(Thong_tin)

#thay doi gia tri 

Thong_tin["Can_nang"]="70kg"

print(Thong_tin["Can_nang"])

#xoa toan bo

print(Thong_tin.clear())
