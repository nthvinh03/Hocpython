import random
import array as ar

while True:
    choose=int(input())
    may=random.randint(0,9)
    if(choose==may):
        print("chinh xac ")
    else:
        print("sai")