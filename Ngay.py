Enter_day=input("Please enter the day of the week (1-7) : ")
Enter_day1=int(Enter_day)
while Enter_day1 <1 or Enter_day1 >7:
    print("Error ! Please re-enter :")
    Enter_day=input("Please enter the day of the week (2-8) : ")
    Enter_day1=int(Enter_day)

week_day=""

if (Enter_day1==1):
    week_day="Monday"
elif Enter_day1==2:
    week_day="Tuesday"
elif Enter_day1==3:
    week_day="Wednesday"
elif Enter_day1==4:
    week_day="Thusday"
elif Enter_day1==5:
    week_day="Friday"
elif Enter_day1 ==6:
    week_day="Saturday"
else :
    wwek_day="Sunday"
print(week_day)
