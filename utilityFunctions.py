import sys
import random
#Global variables
fileInformation = []
algorithmToUse = 0

"""
Function: readInputFile
Input: -
Output: -
Description: Function that read the information from input file and call saveInformationFromFile function
             to convert and save the strings informtation in a list with integers
"""
def readInputFile():
    global algorithmToUse

    fileName = sys.argv[2]
    informationInStr = []

    with open("./Problems/" + fileName) as file:
        lines = file.readlines()

        for line in lines:
            informationInStr.append(line.strip('\n'))

    algorithmToUse =  int(sys.argv[1])

    convertInformationFromFile(informationInStr)

"""
Function: convertInformationFromFile
Input: -
Output: -
Description: Function that converts the information in str format to int format and save it in a list
"""
def convertInformationFromFile(information):
    i = 0

    while i <= len(information) -1:

        if len(information[i].split(",")) > 1:

            numbersInString = []
            
            for number in information[i].split(","):
                numbersInString.append(int(number))

            i += 1
            fileInformation.append(numbersInString)
        
        else:
            fileInformation.append(int(information[i].split(",")[0]))
            i+=1

"""
Utils for Brute Force Algorithm
"""
def RotateBlockBrute(Block):
    for i in range(len(Block)):
            # Obtener un índice aleatorio
            randindex = random.randint(0, len(Block) - 1)
            # Intercambiar
            temp = Block[i]
            Block[i] = Block[randindex]
            Block[randindex] = temp

    return Block

def ReturnThreeCandidates(Block):
    candidates = []

    x = 1
    #longitud
    while x <= 3:

        print(x)
        print("len lista", len(candidates))
        #if len(candidates) <= 3:
        candidate = RotateBlockBrute(Block)
        print("Candidate",candidate)
        if ValidateBlockBrute(candidate):
                print("Agregando:",candidate)
                candidates.append(candidate)
                print(candidates)
                x+=1

    return candidates

def ValidateBlockBrute(Block):

    F = Block[0]
    P = Block[1]
    A = Block[2]

    if(F<=P):
        return True
    return False

"""
Utils for Dynamic Algorithm
"""
def RotateDynamic(Block):
    F = Block[0]
    P = Block[1]
    A = Block[2]

    BlockOne = []
    BlockTwo = []

    if A<=P:
        BlockOne.append(A)
        BlockOne.append(P)
        BlockOne.append(F)
    if P>A:
        BlockTwo.append(A)
        BlockTwo.append(F)
        BlockTwo.append(P)

    candidates = []
    candidates.append(Block)
    if BlockOne!=[]:
        candidates.append(BlockOne)
    if BlockTwo != []:
        candidates.append(BlockTwo)
    return candidates

def GetOptimalHeight(BlockList):
    NewOrder = []

    #for count in range (0,len(BlockList)-1):
    while BlockList!=[]:
        BaseIndex = 0
        BlockBase = [0, 0, 0]
        x = 0
        while x <= len(BlockList)-1:
                #print(BlockBase)

                if BlockList[x][0]>=BlockBase[0] and BlockList[x][1]>=BlockBase[1]:
                    #print(BlockList[x][0],BlockList[x][1])
                    BlockBase = BlockList[x]
                    BaseIndex = x
                x=x+1

        NewOrder.append(BlockBase)
        BlockList.pop(BaseIndex)
        for y in BlockList:
            if y == BlockBase:
                NewOrder.append(BlockBase)
                BlockList.remove(y)

    #print("Blocks:", NewOrder)
    aux = 1
    while aux <= len(NewOrder)-1:
        #print(aux)
        if (NewOrder[aux][0]>NewOrder[aux-1][0]) or (NewOrder[aux][1]>NewOrder[aux-1][1]):
            NewOrder.pop(aux)
        else:
            aux = aux + 1

    height = 0
    for block in NewOrder:
        height = height + block[2]

    #print("BlockList:", BlockList)
    print("Blocks:", NewOrder)
    print("Max Height", height)

def printBlocks(BlockList):
    for block in BlockList:
        print(block)
#readInputFile()
#print(fileInformation)
#print(algorithmToUse)