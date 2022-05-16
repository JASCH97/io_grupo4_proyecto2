import sys
import random
import itertools

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



"""
Function: ReturnThreeCandidates
Input: Block
Output: newPermutation
Description: This function is responsible for creating all the three candidates meaning the block and its rotations
"""

def ReturnThreeCandidates(Block):
    candidates = []

    inp_list = Block
    permutations = list(itertools.permutations(inp_list))

    for block in permutations:
        if ValidateBlockBrute(block):
            candidates.append(list(block))

    newPermutation = []
    for block in candidates:
        if block not in newPermutation:
            newPermutation.append(block)

    return newPermutation

"""
Function: PermuteBlocks
Input: BlockList
Output: ListedPermutations
Description: This function is responsible for creating all the permutations of the matrix BlockList
"""

def PermuteBlocks(BlockList):
    inp_list = BlockList
    permutations = list(itertools.permutations(inp_list))

    ListedPermutations = []
    for block in permutations:
        if ValidateBlockBrute(block):
            ListedPermutations.append(list(block))

    return ListedPermutations

"""
Function: ValidateBlockBrute
Input: Block
Output: Boolean
Description: Validates F <= P
"""

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

"""
Function: RotateDynamic
Input: Block
Output: candidates
Description: Makes the rotation dinamically by setting the base cases
"""
def RotateDynamic(Block):
    F = Block[0]
    P = Block[1]
    A = Block[2]

    BlockZero = []
    BlockOne = []
    BlockTwo = []
    BlockThree = []
    BlockFour = []
    BlockFive = []


    if A<=F and A<=P:
        BlockZero.append(A)
        BlockZero.append(P)
        BlockZero.append(F)
    if A<=P:
        BlockOne.append(A)
        BlockOne.append(P)
        BlockOne.append(F)
    if P>=A:
        BlockTwo.append(A)
        BlockTwo.append(F)
        BlockTwo.append(P)
    if A>=F:
        BlockThree.append(F)
        BlockThree.append(A)
        BlockThree.append(P)
    if P<=A:
        BlockFour.append(P)
        BlockFour.append(A)
        BlockFour.append(F)
    if P<=F:
        BlockFive.append(P)
        BlockFive.append(F)
        BlockFive.append(A)

    candidates = []
    candidates.append(Block)

    if BlockOne!=[]:
        candidates.append(BlockOne)
    if BlockTwo != []:
        candidates.append(BlockTwo)
    if BlockThree != []:
        candidates.append(BlockThree)
    if BlockFour != []:
        candidates.append(BlockFour)
    if BlockFive != []:
        candidates.append(BlockFive)
    return candidates

"""
Function: GetOptimalHeight
Input: BlockList, Argument (Method Used, Brute or Dinamic)
Output: Outcome [Blocks, Height]
Description: Gets the and orders the Block List entered and returns its maximun Height
"""
def GetOptimalHeight(BlockList,Arg):
    #The rearranged Blocklist will be stored in NewOrder
    NewOrder = []

    while BlockList!=[]:
        BaseIndex = 0
        BlockBase = [0, 0, 0]
        x = 0
        while x <= len(BlockList)-1:

                if BlockList[x][0]>=BlockBase[0] and BlockList[x][1]>=BlockBase[1]:
                    BlockBase = BlockList[x]
                    BaseIndex = x
                x=x+1

        NewOrder.append(BlockBase)
        BlockList.pop(BaseIndex)
        for y in BlockList:
            if y == BlockBase:
                NewOrder.append(BlockBase)
                BlockList.remove(y)

    aux = 1
    while aux <= len(NewOrder)-1:
        if (NewOrder[aux][0]>NewOrder[aux-1][0]) or (NewOrder[aux][1]>NewOrder[aux-1][1]):
            NewOrder.pop(aux)
        else:
            aux = aux + 1

    height = 0
    for block in NewOrder:
        height = height + block[2]

    if Arg == "2":
        print("Blocks:", NewOrder)
        print("Max Height:", height)

    outcome = [height,NewOrder]
    return outcome

def printBlocks(BlockList):
    for block in BlockList:
        print(block)
#ReturnThreeCandidates([3, 5, 1])
#readInputFile()
#print(fileInformation)
#print(algorithmToUse)