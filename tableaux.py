import os

class Formula:
    funcao = 0
    tipo = 0
    marca = 1
    primeiroAtomo = 0
    conectivo = 0
    segundoAtomo = 0
    negacao = 1
    def __init__(self, texto):
        if len(texto) == 3:
            self.primeiroAtomo = texto[0]
            self.conectivo = texto[1]
            self.segundoAtomo = texto[2]
            print(self.conectivo)

        elif len(texto) == 2:
            self.negacao = texto[0]
            self.primeiroAtomo = texto[1]
            
        else:
            self.primeiroAtomo = texto[0]

        
            
    
class Marcada:
    marca = 0
    formula = 0
    def __init__(self, marca, formula):
        self.marca = marca
        self.formula = formula

def encontraRegra(formula):
    marca = formula.marca
    conectivo = formula.conectivo

    if conectivo == "¬":
        if marca == 1:
            formula.tipo = "linear"
            formula.funcao = "TrueNegacao"
            return 
        else:
            formula.tipo = "linear"
            formula.funcao = "FalsaNegacao"
            return 
    elif conectivo == "^":
        if marca == 1:
            formula.tipo = "linear"
            formula.funcao = "TrueAeB"
            return "True"
        
        else:
            formula.tipo = "bifurca"
            formula.funcao = "FalseAeB"
            return 
    elif conectivo == "v":
        if marca == 1:
            formula.tipo = "bifurca"
            formula.funcao = "TrueAouB"
            return
        
        else:
            formula.tipo = "linear"
            formula.funcao = "FalseAouB"
            return 
    elif conectivo == ">":
        if marca == 1:
            formula.tipo = "bifurca"
            formula.funcao = "TrueImplicacao"
            return
        else:
            formula.tipo = "linear"
            formula.funcao = "FalseImplicacao"
            return 

#######Lineares
def TrueNegacao(formula):
    novoA = Formula(formula.primeiroAtomo)
    novoA.marca = 0
    novoA.tipo = "atomo"
    ramo.append(novoA)

def FalseNegacao(formula):
    novoA = Formula(formula.primeiroAtomo)
    novoA.marca = 1
    novoA.tipo = "atomo"
    ramo.append(novoA)


def TrueAeB(formula):
    novoA = Formula(formula.primeiroAtomo)
    novoA.marca = 1
    novoA.tipo = "atomo"
    ramo.append(novoA)
    
    novoB = Formula(formula.segundoAtomo)
    novoB.marca = 1
    novoB.tipo = "atomo"
    ramo.append(novoB)
    
    print("TrueAeB")

def FalseAouB(formula):
    novoA = Formula(formula.primeiroAtomo)
    novoA.marca = 0
    novoA.tipo = "atomo"
    ramo.append(novoA)
    
    novoB = Formula(formula.segundoAtomo)
    novoB.marca = 0
    novoB.tipo = "atomo"
    ramo.append(novoB)

def FalseImplicacao(formula):
    novoA = Formula(formula.primeiroAtomo)
    novoA.marca = 1
    novoA.tipo = "atomo"
    ramo.append(novoA)
    
    novoB = Formula(formula.segundoAtomo)
    novoB.marca = 0
    novoB.tipo = "atomo"
    ramo.append(novoB)

######Bifurcam
def FalseAeB(formula, ramo_, index_ja_usadas):
    
    ##index == 1
    ramoCopia = ramo_.copy()
    ramoCopia2 = ramo_.copy()
    
    indexA = len(ramoCopia)
    novoA = Formula(formula.primeiroAtomo)
    novoA.marca = 0
    novoA.tipo = "atomo"
    
    ramoCopia.append(novoA)
    

    if Fechou(novoA, ramoCopia) == False:
        if ProcuraBifurca(ramoCopia, (index_ja_usadas)):
            print("Fechou")
        else:

            print(novoA.marca)
            print(novoA.primeiroAtomo)
            
            print("esse saturou1")
            for i in ramoCopia:
                print(i.primeiroAtomo)
            Saturou()
    else:
         print("realmente fechou")

    ramoCopia = ramoCopia2

    indexB = len(ramoCopia)
    novoB = Formula(formula.segundoAtomo)
    novoB.marca = 0
    novoB.tipo = "atomo"
    ramoCopia.append(novoB)

    if Fechou(novoB, ramoCopia) == False:
        if ProcuraBifurca(ramoCopia, (index_ja_usadas)):
            print("Fechou")
        else:
            print(novoB.primeiroAtomo)
            print("esse saturou2")
            Saturou()
    else:
         print("realmente fechou")   

    return

def TrueAouB(formula, ramo_, index_ja_usadas):
    
    ##index == 1
    ramoCopia = ramo_.copy()
    ramoCopia2 = ramo_.copy()
    
    indexA = len(ramoCopia)
    novoA = Formula(formula.primeiroAtomo)
    novoA.marca = 1
    novoA.tipo = "atomo"
    
    ramoCopia.append(novoA)
    

    if Fechou(novoA, ramoCopia) == False:
        if ProcuraBifurca(ramoCopia, (index_ja_usadas)):
            print("Fechou")
        else:

            print(novoA.marca)
            print(novoA.primeiroAtomo)
            
            print("esse saturou1")
            for i in ramoCopia:
                print(i.primeiroAtomo)
            Saturou()
    else:
         print("realmente fechou")

    ramoCopia = ramoCopia2

    indexB = len(ramoCopia)
    novoB = Formula(formula.segundoAtomo)
    novoB.marca = 1
    novoB.tipo = "atomo"
    ramoCopia.append(novoB)

    if Fechou(novoB, ramoCopia) == False:
        if ProcuraBifurca(ramoCopia, (index_ja_usadas)):
            print("Fechou")
        else:
            print(novoB.primeiroAtomo)
            print("esse saturou2")
            Saturou()
    else:
         print("realmente fechou")   

    return

def TrueImplicacao(formula, ramo_, index_ja_usadas):

    ##index == 1
    ramoCopia = ramo_.copy()
    ramoCopia2 = ramo_.copy()
    
    indexA = len(ramoCopia)
    novoA = Formula(formula.primeiroAtomo)
    novoA.marca = 0
    novoA.tipo = "atomo"
    
    ramoCopia.append(novoA)
    

    if Fechou(novoA, ramoCopia) == False:
        if ProcuraBifurca(ramoCopia, (index_ja_usadas)):
            print("Fechou")
        else:

            print(novoA.marca)
            print(novoA.primeiroAtomo)
            
            print("esse saturou1")
            for i in ramoCopia:
                print(i.primeiroAtomo)
            Saturou()
    else:
         print("realmente fechou")

    ramoCopia = ramoCopia2

    indexB = len(ramoCopia)
    novoB = Formula(formula.segundoAtomo)
    novoB.marca = 1
    novoB.tipo = "atomo"
    ramoCopia.append(novoB)

    if Fechou(novoB, ramoCopia) == False:
        if ProcuraBifurca(ramoCopia, (index_ja_usadas)):
            print("Fechou")
        else:
            print(novoB.primeiroAtomo)
            print("esse saturou2")
            Saturou()
    else:
         print("realmente fechou")   

    return

def ProcuraBifurca(ramoCopia_, index_):
    ramoCopia = ramoCopia_.copy()
    if len(ramo) > index_:
        index_aux = index_
        for i in range((index_ + 1),len(ramo),1):
            print(i)
            #i = i + index
            if ramo[i].tipo == "bifurca":
                print("chamou")
                globals()[ramoCopia[i].funcao](ramoCopia[i], ramoCopia, i)
                return True
        return False
    else:
        return False
def Fechou(formula, ramoCopia_):
    formula_ = formula
    ramoCopia = ramoCopia_.copy()

    for i in range(len(ramoCopia)):
        if formula_.primeiroAtomo == ramoCopia[i].primeiroAtomo and formula_.conectivo == ramoCopia[i].conectivo and formula_.marca != ramoCopia[i].marca:
            print("entrou aq")
            return True

    return False    
def Saturou():
    print("O tablô é aberto, o sequente não é válido")
    os.system("pause")
    quit()



print("insira as formulas")
#pegar as formulas
#formulas = [Formula("P^Q"), Formula("P>Q"), Formula("Q>R")]
formulas = [Formula("P"), Formula("P>Q"), Formula("Q>R")] #progama foi perfeito nessa
#formulas = [Formula("PvQ"), Formula("P>R"), Formula("Q>S")] funciona
#formulas = [Formula("AvB"), Formula("B>C"), Formula("¬C")] funciona
#formulas = [Formula("AvB"), Formula("A>C")]
#formulas = [Formula("A"), Formula("A>B")]
print("insira o sequente")
#pegar o sequente
#sequente = Formula("R^Q")
sequente = Formula("R")
#sequente = Formula("R^S")
#sequente = Formula("C")
#sequente = Formula("C")
#sequente = Formula("B")

sequente.marca = 0
######### PRIMEIRO PASSO
for formula in formulas:
    formula.marcador = 1


################

ramo = []

for i in formulas:
    ramo.append(i)

ramo.append(sequente)
    
for i in ramo:
    encontraRegra(i)

##encontra lineares primeiro
index = -1
for i in ramo:
    index += 1
    if i.tipo == "linear":
        globals()[i.funcao](i)
        ramo.pop(index)


index = -1

for i in ramo:
    index += 1
    if i.tipo == "bifurca":
        print(i.funcao)
        globals()[i.funcao](i, ramo, index)

        print("O tableaux ta fechado, o sequente é valido")
        break



print("fim programa")
