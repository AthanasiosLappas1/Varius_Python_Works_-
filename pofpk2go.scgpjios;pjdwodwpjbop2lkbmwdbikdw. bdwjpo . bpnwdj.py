import random
i=random.randint(1,17)
while True:
    L=[random.randint(0,1),random.randint(1,3),random.randint(3,5),random.randint(5,7),random.randint(7,9),random.randint(9,11),random.randint(11,13),random.randint(13,15),random.randint(15,17)]
    i=i+1
    L.append(random.randint(L[len(L)-1]-1,1+L[len(L)-1]))
    
    print(random.randint(-L[len(L)-1],L[len(L)-1])/i)
