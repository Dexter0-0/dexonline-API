# -----------------------------------------------------------------------------------#
#                               !!Important!!                                        #
#                                                                                    #
#   Dexonline isi declina orice responsabilitate fata de utilizarea                  #
#   programelor sau aplicatiilor existente in aceasta pagina.                        #
#                                                                                    #
#   Nu imi asum responsabilitatea pentru orice "Eroare", probleme sau                #
#   daune cauzatate de acest cod                                                     #
#                                                                                    #
#   This program is free software: you can redistribute it and/or modify it          #
#   under the terms of the GNU General Public License as published by the  Free      #
#   Software Foundation, either version 3 of the License, or (at your option)        #
#   any later version.                                                               #
#                                                                                    #
#   This program is distributed in the hope that it will be useful, but WITHOUT      #
#   ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
#   FOR  A PARTICULAR PURPOSE.  See the GNU General Public License for more details. #
#                                                                                    #
#   You should have received a copy of the GNU General Public License                #
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.           #
#                                                                                    #
# -----------------------------------------------------------------------------------#

try:
    from lxml import html
except ImportError:
    print("lxml lipseste (pip install lxml)")

try:
    import requests
except ImportError:
    print("requests lipseste (pip install requests)")

try:
    import unidecode
except ImportError:
    print("unidecode lipseste (pip install unidecode )")

try:
    import datetime
except ImportError:
    print("datetime lipseste (pip install datetime )")


def NumarCuvintePrefix(Prefix):
    try:
        PrefixPage = "https://dexonline.net/cuvinte-care-incep-cu-" + Prefix
        Tree = html.fromstring(requests.get(PrefixPage).content)
        return int(Tree.xpath('count(//a)') - 13)
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def NumarCuvinteSufix(Sufix):
    try:
        SufixPage = "https://dexonline.net/cuvinte-care-se-termina-cu-" + Sufix
        Tree = html.fromstring(requests.get(SufixPage).content)
        return int(Tree.xpath('count(//a)') - 13)
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def NumarCuvinteRima(Cuvant, GradulRimei=1):
    try:
        RhymePage = "https://dexonline.net/rime-" + Cuvant + "-gradul-" + str(GradulRimei)
        Tree = html.fromstring(requests.get(RhymePage).content)

        if int(Tree.xpath('count(//a)') - 43) <= 0:
            return 0
        return int(Tree.xpath('//html/body/div/div[2]/h3/span/text()')[0].replace("(", "").replace(")", ""))
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def NumarCuvinteSinonim(Cuvant):
    try:
        SynonymousPage = "https://dexonline.net/sinonime-" + Cuvant
        Tree = html.fromstring(requests.get(SynonymousPage).content)
        SynonymousNumber = len(Tree.xpath('/html/body/div/div[2]/div[2]/div/p/i/text()')) + 1

        if SynonymousNumber <= 1:
            return 0
        return SynonymousNumber
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def NumarCuvinteAntonime(Cuvant):
    try:
        AntonymousPage = "https://dexonline.net/sinonime-" + Cuvant
        Tree = html.fromstring(requests.get(AntonymousPage).content)
        AntonymousNumber = len(Tree.xpath('/html/body/div/div[2]/div[2]/div/p/i/text()')) + 1

        if AntonymousNumber <= 1:
            return 0
        return AntonymousNumber
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def CuvintePrefix(Prefix, NumarCuvinte=0):
    try:
        PrefixPage = "https://dexonline.net/cuvinte-care-incep-cu-" + str(Prefix)
        Tree = html.fromstring(requests.get(PrefixPage).content)
        Words = []

        PageNumber = len(Tree.xpath('/html/body/div/ul/li'))

        if PageNumber == 0:
            PageNumber = 1

        for Page in range(1, PageNumber + 1):
            Tree = html.fromstring(requests.get(PrefixPage + '/' + str(Page)).content)

            for Row in range(1, len(Tree.xpath('/html/body/div/div[3]/div/div'))):
                for Word in range(1, len(Tree.xpath('/html/body/div/div[3]/div/div[' + str(Row) + ']/a/text()')) + 1):
                    Words.append((str(
                        Tree.xpath('/html/body/div/div[3]/div/div[' + str(Row) + ']/a[' + str(Word) + ']/text()')).replace("[", "").replace("]", "").replace("'", "")))
                    if NumarCuvinte != 0 and len(Words) == NumarCuvinte:
                        return Words
        return Words
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def CuvinteSufix(Sufix, NumarCuvinte=0):
    try:
        SufixPage = "https://dexonline.net/cuvinte-care-se-termina-cu-" + str(Sufix)
        Tree = html.fromstring(requests.get(SufixPage).content)
        Words = []

        PageNumber = len(Tree.xpath('/html/body/div/ul/li'))

        if PageNumber == 0:
            PageNumber = 1

        for Page in range(1, PageNumber + 1):
            Tree = html.fromstring(requests.get(SufixPage + '/' + str(Page)).content)

            for Row in range(1, len(Tree.xpath('/html/body/div/div[3]/div/div'))):
                for Word in range(1, len(Tree.xpath('/html/body/div/div[3]/div/div[' + str(Row) + ']/a/text()')) + 1):
                    Words.append((str(
                        Tree.xpath('/html/body/div/div[3]/div/div[' + str(Row) + ']/a[' + str(Word) + ']/text()')).replace(
                        "[", "").replace("]", "").replace("'", "")))
                    if NumarCuvinte != 0 and len(Words) == NumarCuvinte:
                        return Words
        return Words
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def CuvinteRima(Cuvant, GradulRimei=1, NumarCuvinte=0):
    try:
        RhymePage = "https://dexonline.net/rime-" + Cuvant + "-gradul-" + str(GradulRimei)
        Tree = html.fromstring(requests.get(RhymePage).content)
        Words = []

        for Row in range(1, len(Tree.xpath('/html/body/div/div[2]/div/div'))):
            for Word in range(1, len(Tree.xpath('/html/body/div/div[2]/div/div[' + str(Row) + ']/a/text()')) + 1):
                Words.append((str(
                    Tree.xpath('/html/body/div/div[2]/div/div[' + str(Row) + ']/a[' + str(Word) + ']/text()')).replace("[","").replace("]", "").replace("'", "")))
                if NumarCuvinte != 0 and len(Words) == NumarCuvinte:
                    return Words
        return Words
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def CuvinteSinonim(Cuvant, NumarCuvinte=0):
    try:
        SynonymousPage = "https://dexonline.net/sinonime-" + Cuvant
        Tree = html.fromstring(requests.get(SynonymousPage).content)
        Words = Tree.xpath('/html/body/div/div[2]/div[2]/div/p/i/text()')

        while (", " in Words):
            Words.remove(", ")

        for i in range(len(Words)):
            Words[i] = Words[i].replace(", ", "").replace(".", "")

        Words2 = Tree.xpath('/html/body/div/div[2]/div[2]/div/p/i/a/text()')

        for i in range(len(Words2)):
            Words.append(Words2[i])

        if NumarCuvinte != 0:
            return Words[:NumarCuvinte]
        else:
            return Words
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def CuvinteAntonim(Cuvant, NumarCuvinte=0):
    try:
        AntonymousPage = "https://dexonline.net/antonime-" + Cuvant
        Tree = html.fromstring(requests.get(AntonymousPage).content)
        Words = Tree.xpath('/html/body/div/div[2]/div[2]/div/p/i/text()')

        while (", " in Words):
            Words.remove(", ")

        for i in range(len(Words)):
            Words[i] = Words[i].replace(", ", "").replace(".", "")

        Words2 = Tree.xpath('/html/body/div/div[2]/div[2]/div/p/i/a/text()')

        for i in range(len(Words2)):
            Words.append(Words2[i])

        if NumarCuvinte != 0:
            return Words[:NumarCuvinte]
        else:
            return Words
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def DefinitieCuvant(Cuvant, NumarDefinitii=0, TipDictionar=0):
    try:
        # Broken af momentan
        WordPage = "https://dexonline.ro/definitie/" + str(Cuvant) + "/expandat"
        Tree = html.fromstring(requests.get(WordPage).content)

        Contents = Tree.xpath('/html/body/div[1]/main/div/div/div[1]/div[2]/p/span[1]/text()')
        return "Work in progress"
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def DeclinariCuvant():
    try:
        return "Work in progress"
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def SintezaCuvant():
    try:
        return "Work in progress"
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def CuvantulZilei(Data="0"):
    try:
        if Data == "0":
            Data = str(datetime.datetime.now())[:10].replace("-", "/")

        WordPage = "https://dexonline.ro/cuvantul-zilei/" + Data
        Tree = html.fromstring(requests.get(WordPage).content)
        Word = unidecode.unidecode(
            str(Tree.xpath('/html/body/div[1]/main/div/div[2]/div[2]/div[2]/p/span/b[1]/text()')[0]).replace(",","").lower().replace("è", "s").replace("è", "t").replace("ã", "i"))
        return Word
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def CuvantulLunii(Data="0"):
    try:
        if Data == "0":
            Data = str(datetime.datetime.now())[:7].replace("-", "/")

        WordPage = "https://dexonline.ro/cuvantul-lunii/" + Data
        Tree = html.fromstring(requests.get(WordPage).content)
        Word = unidecode.unidecode(
            str(Tree.xpath('/html/body/div[1]/main/div/div/div[2]/div[2]/p/span/b[1]/text()')[0]).replace(",", "").lower().replace("è", "s").replace("è", "t").replace("ã", "i"))
        return Word
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def ArticolulLunii():
    try:
        return "Work in progress"
    except RuntimeError:
        print("Ceva nu a functionat :((((")


def CuvantAleatoriu():
    try:
        # salut ba dexter
        CuvantAleatoriu = requests.get('https://dexonline.ro/ajax/randomWord.php')
        return CuvantAleatoriu.text
    except RuntimeError:
        print("Ceva nu a functionat :((((")
