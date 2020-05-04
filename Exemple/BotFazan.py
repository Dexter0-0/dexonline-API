if __name__ == '__main__':
    #Game Loop
    while True:
        #Ia cuvantul ales de jucator
        print("Scrie un cuvant")
        CuvantAles = str(input())

        #Ia sufixul cuvantului ales si stocheaza cuvinte care incep cu el
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

            #Scorul este invers proportional cu numarul de cuvinte care incep cu sufixul cuvintelor din lista
            Scor = 1 / NumarCuvintePrefix(Cuvinte[i][-2] + Cuvinte[i][-1]) * 1000

            #Print cu scorul si cuvantul pentru a demonstra procesul
            print(i, "-", Cuvinte[i], ":", Scor)

            #Memoreaza cel mai bun cuvant
            if Scor > MaxScor:
                MaxScor = Scor
                CuvantFinal = Cuvinte[i]

            #50 e suficient de bun pentru a inchide un jucator asa ca nu mai are rost sa mai caute
            if MaxScor > 50:
                break

        #Arata cuvantul gasit
        print("Cuvantul ales este", CuvantFinal)
