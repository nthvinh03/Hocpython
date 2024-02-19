a=input()

b=float(a)

c=""

if b%2==0:
    c="even"
elif b%2==1:
    c="not an even"
else:
    c="not a natural number"
print(c)