import random
I=0
WIN = 0
LOSS=0
WON=0
while True:
        I+=1
        Guess=int(input("Guess_an_Integer!!!"))
        CPU_guess = random.uniform(0,Guess*Guess)
        if Guess >=CPU_guess:
                WIN+=1
                WON+= Guess-CPU_guess
                print("Lucky BOYA",WIN)
        else:
                LOSS+=1
                print("Try AGAIN???")
                print(I,"NUMBER OF GUESSES. CPU GUESS'ES RIGHT: *()*", CPU_guess)
        print("WINS TO LOOSE RATIO:",WIN, "LOSSES:",LOSS)
        quit0=int(input("QUIT???"))
        if quit0==0:
                print("ONLY WON:", WON,".... YOU .............. WHY ?>????>< :_")
                break
if LOSS==0:
        print("OUR CHAAAAAAAAMPIOOOOOOOOOOOOOOOOOOOOOOOOOOOONNNNNNNNNNN...... !!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
elif WIN==LOSS:
        print(" A TIE ??????????????? x|||")
elif  WIN/LOSS > 1:
        print("YOU WON !!!!!!!!!! AND 'ONLY' BY !!!!!!!!!!!! :", WIN/LOSS)
elif WIN/LOSS < 1:
        print(" YOU LOOOOOOOOOOOOOOOOSEEEEEEEEEEEEE....... XD XD XD . WITH LOOSE RATIO... : !!!", LOSS)
else:
        print("YOU TIED !!!!!!!! LUCKY NUMBER 1; or 0??? : ) ; ) : ) !!! ( ;))")
print("credits... :",WON)
