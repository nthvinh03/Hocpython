tieng_anh=['hi','bye','love']
tieng_viet=['chao','tam biet','yeu']

str_input=input("nhap 1 trong cac gia tri cua tieng anh : ")

for i in range(len(tieng_anh)):
    if str_input==tieng_anh[i]:
        tieng_anh[i]=tieng_viet[i]
        print(tieng_viet[i])


    