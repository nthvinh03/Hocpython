convert={
    'Hello':'Xin chao',
    'Goodbye':'Tam biet',
    'Goodluck':'Chuc may man',
    'See you again':'Hen gap lai'
}





def display_convert(convert_db,tt):
    for i in convert_db:
        if i == tt:
            print(i," : ",convert_db[i])
    
input_tt=input("Enter : ")
if input_tt in convert:
    display_convert(convert,input_tt)
else:
    print(input_tt+ " not in database")