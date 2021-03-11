"""
Fernando Andres Chavez Gavaldon
SEND + MORE = MONEY
"""

contador = 0
alpha=0
for S in range(10):
    for E in range(10):
        if E==S: continue
        for N in range(10):
            if N == E or N == S: continue
            for D in range(10):
                if D==N or D==E or D==S: continue
                for M in range(10):
                    if M==D or M==N or M==E or M==S: continue
                    for O in range(10):
                        if O==M or O==D or O==N or O==E or O==S: continue
                        for R in range(10):
                            if R==O or R==M or R==D or R==N or R==E or R==S: continue
                            for Y in range (10):
                                if Y==R or Y==O or Y==M or Y==D or Y==N or Y==E or Y==S: continue
                                SEND  =           S*1000 + E*100 + N*10 + D
                                MORE  =           M*1000 + O*100 + R*10 + E
                                MONEY = M*10000 + O*1000 + N*100 + E*10 + Y
                                alpha +=1

                                if SEND+MORE==MONEY:
                                    contador += 1
                                    print(" ",S,E,N,D,"\n+",M,O,R,E,"\n__________","\n",M,O,N,E,Y,"\n")
                                    print("S=",S," E=",E," N=",N," D=",D," M=",M," O=",O," R=",R," Y=",Y,"\n\n")



print(contador,"\n",alpha)