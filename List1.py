S='1 2 3 4 5 6'

S1=S.split()

S2= 'a'.join(S1[::-1])+ 'a'

print(S2)
