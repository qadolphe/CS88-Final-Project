"""
want to do statistical tests to prove this is random
"""
#from doublePendulumWrite import *
import matplotlib.pyplot as plt

#test 1 dictionary test to find multiples
errors = []

d = set()
val_lst = []
dups = {}
totalDups = 0
ini_str = "0123456789"
permutationDict = {}


def initFiles(filename):
    f = open(filename, "r")
    valString = ""
    totalDups = 0
    for i in f:
        
        
        v = str(int(i))
        valString = valString + v
        if i in d:
            totalDups +=1
            try:
                dups[i]+=1
            except:
                dups[i] = 1 
            
        else:
            d.add(i)
            #permutationDict[i] = 0
            val_lst.append(int(i))
    return valString
        
        
        
    
    
            

def findMultiples():
    print("PRINTING DUPS: \n")
    count = 0
    maxi = 0
    for i in dups:
        if dups[i] > 1:
            count +=1
            print(str(i)+" was found "+str(dups[i])+" times")
            if dups[i]>maxi:
                maxi = dups[i]
    print("\n"+str(count)+" duplicates found")
    print("\n"+str(maxi)+" was the highest count for a single value")

#birthday 
#overlapping permutations



#finding 5 consecutive values
def permutationTest(valString):
    x = []
    print("\nFINDING PERMUTATIONS:\n")
    permslst = [12345, 12354, 12435, 12453, 12534, 12543, 13245, 13254, 13425, 13452, 13524, 13542, 14235, 14253, 14325, 14352, 14523, 14532, 15234, 15243, 15324, 15342, 15423, 15432, 21345, 21354, 21435, 21453, 21534, 21543, 23145, 23154, 23415, 23451, 23514, 23541, 24135, 24153, 24315, 24351, 24513, 24531, 25134, 25143, 25314, 25341, 25413, 25431, 31245, 31254, 31425, 31452, 31524, 31542, 32145, 32154, 32415, 32451, 32514, 32541, 34125, 34152, 34215, 34251, 34512, 34521, 35124, 35142, 35214, 35241, 35412, 35421, 41235, 41253, 41325, 41352, 41523, 41532, 42135, 42153, 42315, 42351, 42513, 42531, 43125, 43152, 43215, 43251, 43512, 43521, 45123, 45132, 45213, 45231, 45312, 45321, 51234, 51243, 51324, 51342, 51423, 51432, 52134, 52143, 52314, 52341, 52413, 52431, 53124, 53142, 53214, 53241, 53412, 53421, 54123, 54132, 54213, 54231, 54312, 54321]
    perms = {12345, 12354, 12435, 12453, 12534, 12543, 13245, 13254, 13425, 13452, 13524, 13542, 14235, 14253, 14325, 14352, 14523, 14532, 15234, 15243, 15324, 15342, 15423, 15432, 21345, 21354, 21435, 21453, 21534, 21543, 23145, 23154, 23415, 23451, 23514, 23541, 24135, 24153, 24315, 24351, 24513, 24531, 25134, 25143, 25314, 25341, 25413, 25431, 31245, 31254, 31425, 31452, 31524, 31542, 32145, 32154, 32415, 32451, 32514, 32541, 34125, 34152, 34215, 34251, 34512, 34521, 35124, 35142, 35214, 35241, 35412, 35421, 41235, 41253, 41325, 41352, 41523, 41532, 42135, 42153, 42315, 42351, 42513, 42531, 43125, 43152, 43215, 43251, 43512, 43521, 45123, 45132, 45213, 45231, 45312, 45321, 51234, 51243, 51324, 51342, 51423, 51432, 52134, 52143, 52314, 52341, 52413, 52431, 53124, 53142, 53214, 53241, 53412, 53421, 54123, 54132, 54213, 54231, 54312, 54321}

    for k in perms:
        permutationDict[k] = 0

    temp = 0
    for i in range(0, len(valString)-6):
        
        curr = valString[i:i+5]
        
        
        if int(curr) in perms:
            permutationDict[int(curr)] += 1

    for j in permslst:
        print(str(j)+" : "+("-"*permutationDict[j]) + str(permutationDict[j]))
        x.append(permutationDict[j])
    return x
    #display results




#minimum distance test
"""
This code was found on geeksforgeeks
"""
def minDist(arr, n, x, y):
    min_dist = 99999999
    for i in range(n):
        for j in range(i + 1, n):
            if (x == arr[i] and y == arr[j] or
                    y == arr[i] and x == arr[j]) and min_dist > abs(i-j):
                min_dist = abs(i-j)
        return min_dist


#chi squared test


    

        
        

def main():
    #p = pendulum()
    initFiles("8P-2.56Sec3.csv")
    findMultiples()
    '''print("here")
    v = initFiles("8P-10000Sec.csv")
    findMultiples()

    print("\n \n")
    v2 = initFiles("8P-10000Sec2.csv")
    
    
    vals = permutationTest(v)
    vals2 = permutationTest(v2)
    print("\n\n\n")
    permslst = [12345, 12354, 12435, 12453, 12534, 12543, 13245, 13254, 13425, 13452, 13524, 13542, 14235, 14253, 14325, 14352, 14523, 14532, 15234, 15243, 15324, 15342, 15423, 15432, 21345, 21354, 21435, 21453, 21534, 21543, 23145, 23154, 23415, 23451, 23514, 23541, 24135, 24153, 24315, 24351, 24513, 24531, 25134, 25143, 25314, 25341, 25413, 25431, 31245, 31254, 31425, 31452, 31524, 31542, 32145, 32154, 32415, 32451, 32514, 32541, 34125, 34152, 34215, 34251, 34512, 34521, 35124, 35142, 35214, 35241, 35412, 35421, 41235, 41253, 41325, 41352, 41523, 41532, 42135, 42153, 42315, 42351, 42513, 42531, 43125, 43152, 43215, 43251, 43512, 43521, 45123, 45132, 45213, 45231, 45312, 45321, 51234, 51243, 51324, 51342, 51423, 51432, 52134, 52143, 52314, 52341, 52413, 52431, 53124, 53142, 53214, 53241, 53412, 53421, 54123, 54132, 54213, 54231, 54312, 54321]
    for j in range(len(permslst)-1):
        q = vals[j]-vals2[j]
        if q<1:
            q = q*(-1)
        print(str(permslst[j])+" : "+("-"*q) + str(q))
    '''
    return 0


main()
