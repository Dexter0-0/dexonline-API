#-------------------------------------------------------------------------------------#
#                                   !!Important!!                                     #
#                                                                                     #
#       Acesta nu este un bot de fazan complet functional ci doar o demonstratie de   #
#   folosire a functilor din acest API asa ca probabil ca are multe buguri dar va     #
#   indemn sa il folositi ca un punct de pornire petru un bot complet de fazan sau    #
#   drept inspiratie pentru alte proiecte care folosesc acest API!! :)))              #
#                                                                                     #
#-------------------------------------------------------------------------------------#

if __name__ == '__main__':
    #Game Loop
    while True:
        #Ia cuvantul ales de jucator
        print("Scrie un cuvant")
        CuvantAles = str(input())

        #Ia sufixul cuvantului ales si stocheaza cuvinte care incep cu el 
        #folosind functia "CuvintePrefix()"
        SufixCuvant = CuvantAles[-2] + CuvantAles[-1]
        Cuvinte = CuvintePrefix(SufixCuvant)
        MaxScor = 0

        #Trece prin toate cuvintele care incep cu sufixul cuvantului ales si le atribuie un scor
        for i in range(len(Cuvinte)):
            #Dex online nu accepta cuvintele in linkuri daca au diacritice (cuvinte care incep cu "șa vor fi 0")
            Cuvinte[i] = Cuvinte[i].lower()
            Cuvinte[i] = Cuvinte[i].replace("ă", "a")
            Cuvinte[i] = Cuvinte[i].replace("â", "a")
            Cuvinte[i] = Cuvinte[i].replace("ș", "s")
            Cuvinte[i] = Cuvinte[i].replace("ț", "t")
            Cuvinte[i] = Cuvinte[i].replace("î", "i")

            #Scorul este invers proportional cu numarul de cuvinte care incep cu sufixul cuvintelor din lista.
            #Numarul de cuvinte este obtinut folosind functia "NumarCuvintePrefix()"
            Scor = 1 / NumarCuvintePrefix(Cuvinte[i][-2] + Cuvinte[i][-1]) * 1000

            #Print cu scorul si cuvantul pentru a arata procesul
            print(i, "-", Cuvinte[i], ":", Scor)

            #Memoreaza cel mai bun cuvant
            if Scor > MaxScor:
                MaxScor = Scor
                CuvantFinal = Cuvinte[i]

            #50 e suficient de bun pentru a inchide un jucator asa ca nu mai are rost sa mai caute
            if MaxScor > 50:
                break

        #Print cu cuvantul gasit
        print("Cuvantul ales este", CuvantFinal)
