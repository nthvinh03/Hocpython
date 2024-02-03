
row = ""
for i in range(1, 11):
    for j in range(2, 10):
        row = row + str(j) + " x " + str(i) + " = " + str(i*j) + "\t"
    print(row)
    row = ""