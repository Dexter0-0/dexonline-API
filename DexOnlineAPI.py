from lxml import html
import requests

def NumarCuvintePrefix(Prefix):
    PrefixPage = "https://dexonline.net/cuvinte-care-incep-cu-" + Prefix
    Tree = html.fromstring(requests.get(PrefixPage).content)
    return int(Tree.xpath('count(//a)') - 13)

def NumarCuvinteSufix(Sufix):
    SufixPage = "https://dexonline.net/cuvinte-care-se-termina-cu-" + Sufix
    Tree = html.fromstring(requests.get(SufixPage).content)
    return int(Tree.xpath('count(//a)') - 13)

def NumarCuvinteRima(Cuvant, GradulRimei = 1):
    RhymePage = "https://dexonline.net/rime-" + Cuvant + "-gradul-" + str(GradulRimei)
    Tree = html.fromstring(requests.get(RhymePage).content)

    #Nu exista rime
    if int(Tree.xpath('count(//a)') - 43) <= 0:
        return 0
    return int(Tree.xpath('//html/body/div/div[2]/h3/span/text()')[0].replace("(","").replace(")",""))

def NumarCuvinteSinonim(Cuvant):
    SynonymousPage = "https://dexonline.net/sinonime-" + Cuvant
    Tree = html.fromstring(requests.get(SynonymousPage).content)
    SynonymousNumber = len(Tree.xpath('/ html / body / div / div[2] / div[2] / div / p / i/text()')) + 1

    #Nu exista sinonime
    if SynonymousNumber <= 1:
        return 0
    return SynonymousNumber

def NumarCuvinteAntonime(Cuvant):
    AntonymousPage = "https://dexonline.net/sinonime-" + Cuvant
    Tree = html.fromstring(requests.get(AntonymousPage).content)
    AntonymousNumber = len(Tree.xpath('/ html / body / div / div[2] / div[2] / div / p / i/text()')) + 1

    #Nu exista antonime
    if AntonymousNumber <= 1:
        return 0
    return AntonymousNumber
