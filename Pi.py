#lappas Athanasios, 13/5/2021, reach at me @ AthanasiosLappas@outlook.com.gr

calculation_limit=int(input("You may input number of loops (enter a sensible number, e.g. 10000"))
start=3
i=1
cont=0
pre=+1
p=input("Do you want the series convergance of the series? (enter 'y'/'anykey'")
while(i<calculation_limit):
    cont=(i+1)*(i+2)*(i+3)
    start=start+4/cont*pre
    pre=pre*-1
    i=i+2
    if(p=="y" or p=="yes"):
        print(start)
print("Calculation ended at:", start)
input("press Enter to exit.")

