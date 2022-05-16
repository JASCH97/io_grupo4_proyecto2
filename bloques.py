import sys
import utilityFunctions

"""
Function: blockTowerBruteForce
Input: BlockList
Output: -
Description: This function is responsible of receiving the Blocks initially set in order 
to rotate them and call its respective functions to rearranged them in 
order to the get the maximun value of the fittest candidate, which is going to be the Output
"""

def blockTowerBruteForce(BlockList):
        print("Fuerza Bruta")
        print("Input:", arg2)
        utilityFunctions.printBlocks(BlockList)
        BlocksToPerm = []
        for Block in BlockList:
            #Block = BlockList[4]
            BlockChildren = utilityFunctions.ReturnThreeCandidates(Block)
            for block in BlockChildren:
                BlocksToPerm.append(block)

        print(BlocksToPerm)

        Permutations = utilityFunctions.PermuteBlocks(BlocksToPerm)
        OptimalCandidate = None
        OptimalHeight = 0
        for perm in Permutations:
            permAux = perm.copy()
            Outcome = utilityFunctions.GetOptimalHeight(perm,arg1)
         
            Height = Outcome[0]
            NewOrder = Outcome[1]
            if Height > OptimalHeight:
                OptimalCandidate = NewOrder
                
                OptimalHeight = Height

        print("Blocks:",OptimalCandidate)
        print("Max Height:",OptimalHeight)

"""
Function: blockTowerDynamic
Input: BlockList
Output: -
Description: This function is responsible of receiving the Blocks initially set in order 
to rotate them and call its respective functions to rearranged them in 
order to the get the maximun value of the fittest candidate by validating the base cases, which is going to be the Output
"""

def blockTowerDynamic(BlockList):
    print("Dinamico")
    print("Input:",arg2)
    utilityFunctions.printBlocks(BlockList)

    Blocks = []
    for Block in BlockList:
        BlockChildren = utilityFunctions.RotateDynamic(Block)
        for BlockAux in BlockChildren:
            Blocks.append(BlockAux)

    utilityFunctions.GetOptimalHeight(Blocks,arg1)


"""
save the first argument (second position in argv list) to a variable
"""
arg1 = sys.argv[1]
arg2 = sys.argv[2]

a_file = open(arg2, "r")

"""
Returns the .txt file in a list
"""
list_of_lists = []
for line in a_file:
  stripped_line = line.strip().replace(",","")
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

a_file.close()

for i in range(len(list_of_lists)):
    for j in range(len(list_of_lists[i])):
        list_of_lists[i][j] = int(list_of_lists[i][j])
        
"""
Choose Algorythm in the terminal
"""
if arg1 == "1":
    blockTowerBruteForce(list_of_lists)
elif arg1 == "2":
    blockTowerDynamic(list_of_lists)
else:
    print("Choose an algorythm")