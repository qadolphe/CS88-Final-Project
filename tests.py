"""
want to do statistical tests to prove this is random
"""
from doublePendulumNoPlot import *

#test 1 dictionary test to find multiples
errors = []
valString = ""
d = set()
val_lst = []
dups = {}
totalDups = 0
ini_str = "0123456789"
permutationDict = {}


def initFiles():
    f = open("8P-1Sec.txt", "r")
    for i in f:
        if d[i]:
            totalDups +=1
            if dups[i]:
                dups[i]+=1
            else:
                dups[i] = 1 
            
        else:
            d.add(i)
            permutationDict[i] = 0
            val_lst.append(int(i))
        valString = valString + i
    
            

def findMultiples():
    for i in dups:
        print(dups[i])

#birthday 
#overlapping permutations
totalPerms = []
def permute(data, i, length): 
    if i == length: 
        totalPerms.append(''.join(data) )
    else: 
        for j in range(i, length): 
            # swap
            data[i], data[j] = data[j], data[i] 
            permute(data, i + 1, length) 
            data[i], data[j] = data[j], data[i]  



def permutationTest():
    permute(list(ini_str), 0, len(ini_str))
    temp = 0
    for i in range(0, len(valString)-6):
        permutationDict[valString[i,i+5]] +=1
    
    #display results
        
        



#minimum distance test

    


def main():
    p = pendulum()

