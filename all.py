L=[1,3,5,7,9,11,13,15,17]
integer=0
Integers = [0,integer]
i=integer
integer = integer + 1
Integers=[1]
for integer in Integers:
    while integer > 0 :
        for integer in L:
            I = L[integer]
            Integers.append(L[integer])
            L.append(I)
            integer=Integers[0]
            print(I)
            if len(L) > I[integer-1]:
                break
            
            
