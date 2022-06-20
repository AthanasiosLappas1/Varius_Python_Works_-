import random
I=0
WIN = 0
LOSS=0
while True:
	I+=1
	Guess=int(input("Guess_a_numbA!!!"))
	CPU_guess = random.uniform(-Guess*Guess,Guess*Guess)
	if Guess >=CPU_Guess:
		WIN+=1
		print("Lucky BOYA",WIN)
	else:
		LOSS+=1
		print("Try AGAIN???")
		print(I,"NUMBER OF GUESSES. CPU GUESS'ES RIGHT: *()*", CPU_Guess, ",YOU LOST:", LOSS, "OUT OF", I, " TIMES.", " YOU WON:",WIN,"TIMES.")
	print("WIN TO LOOSE RATIO:",WIN/LOSS)
	quit0=int(input("QUIT??? PRESS ZERO AND ENTER ... OR ANY NUMBA TO CONTINUE,,, !!! !!! YOU TRIED SUCCESFULLY :",WIN/I"OF THE TIMES !!!!"))
	if quit0==0:
		break
if  WIN/LOSS > 1:
	print("YOU WON !!!!!!!!!!", WIN/LOSS)
elif WIN/LOSS < 1:
	print(" YOU LOOOOOOOOOOOOOOOOSEEEEEEEEEEEEE....... XD XD XD . !!!", LOSS/WIN)
else:
	print("YOU TIED !!!!!!!! LUCKY NUMBER 1; or 0??? : ) ; ) : ) !!! ( ;))")	
