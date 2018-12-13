from random import *
import math

def generateRandom(length=39):
    array = [chr(i+97) for i in range(26)]+[' ', ',', '!', '.']+[chr(j+65) for j in range(26)]
    stri = ''
    for i in range (length) :
        rand = randint(0, len(array)-1)
        stri += array[rand]
    return stri

def getFitness(stri, base) :
    return sum(0 if stri[i] == base[i] else 1 for i in range(len(stri)) )

def getPregnant(parents, base) :
    children = ''
    for i in range(len(parents[0])) :
        r = randrange(0,2)
        children += parents[r][i]
    fitness = getFitness(children, base)
    if children != base :
        try :
            r1 = randrange(0,len(base))
        except :
            r1 = 0
        children = children[:r1]+generateRandom(1)+children[r1+1:]
    return [fitness, children]


def newGeneration(current, base):
    t = sum(sum(j for j in range(i)) for i in range (len(base)))
    newGeneration = []
    for i in range (len(current)) :
        summ = 0
        parents = []
        while len(parents) < 2 :
            r = randint(0, t)
            for i in range(len(current)) :
                summ += sum(j for j in range(i))
                if summ >= r :
                    parents.append(current[i][1])
                    break
        newGeneration.append(getPregnant(parents, base))
    return sorted(newGeneration, key=lambda x: x[0])

s = 'GLorem Ipsum is simply dummy text of the printing and typesetting industry.'

generation = []
for x in range(1000) :
    r = generateRandom(len(s))
    generation.append([getFitness(r, s), r])

generation = sorted(generation, key=lambda x: x[0])

nGen = 0
while generation[-1][1] != s :
    nGen +=1
    generation = newGeneration(generation, s)
    print(nGen, ' - ', generation[-1])
