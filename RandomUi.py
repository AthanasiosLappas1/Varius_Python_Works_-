import random
a=0
B=0
i=1
while True:
	a=random.uniform(-a,a)
	B=B+a
	a=a+1
	if i > 1000000:
		break
print(B, B/i)



