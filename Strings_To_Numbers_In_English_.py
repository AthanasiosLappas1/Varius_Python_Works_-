#Athanasios Lappas25/7/2022 01:07 (Eastern time +2 ).
#Programm to calculate the arithmetic values of words or letters in English.
#Many interesting Stuff may occure !!!
while True:
    AB=['A','B','C','D','E','F','G','H','I','j','K','L','M','N','O','P','W','R','S','T','U','V','W','X','Y','Z']
    ABN=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    WR = input("Give me the word or sentence to find you the sum of the arithmetically ascending order. !  :")
    wr = list(WR)
    sumw=0
    for letter in wr:
        for j in range(0,25):
            if letter.upper() == AB[j]:
                sumw += ABN[j]
    print("Result =",sumw)
