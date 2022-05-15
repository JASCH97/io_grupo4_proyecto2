import sys
import utilityFunctions

# Frente (F), Profundidad (P) y Altura (A) donde F <= P
# Los bloques se pueden rotar en sus dimensiones, y se pueden usar más de un bloque según
# las rotaciones del mismo tipo para formar la torre. Cada bloque tiene 3 posibles rotaciones.
# Manteniendo siempre el Frente menor o igual que la Profundidad. Ejemplo bloque
# {FxPxA} de {2x3x1} solo puede tener 3 posiciones {2x3x1}, {1x2x3} y {1x3x2}.



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
            #print(Height)
            Height = Outcome[0]
            NewOrder = Outcome[1]
            if Height > OptimalHeight:
                OptimalCandidate = NewOrder
                #print(permAux)
                OptimalHeight = Height

        print("Blocks:",OptimalCandidate)
        print("Max Height:",OptimalHeight)
        #BlockChild = utilityFunctions.RotateBlockBrute(Block)
        #print(BlockChild)
        #if(utilityFunctions.ValidateBlockBrute(BlockChild)):
            #print("True")
        #else:
            #print("False")

def blockTowerDynamic(BlockList):
    print("Dinamico")
    print("Input:",arg2)
    utilityFunctions.printBlocks(BlockList)

    Blocks = []
    for Block in BlockList:
        BlockChildren = utilityFunctions.RotateDynamic(Block)
        for BlockAux in BlockChildren:
            Blocks.append(BlockAux)

    #print(Blocks)
    utilityFunctions.GetOptimalHeight(Blocks,arg1)


# save the first argument (second position in argv list) to a variable
arg1 = sys.argv[1]
arg2 = sys.argv[2]

a_file = open(arg2, "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip().replace(",","")
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

a_file.close()

for i in range(len(list_of_lists)):
    for j in range(len(list_of_lists[i])):
        list_of_lists[i][j] = int(list_of_lists[i][j])

if arg1 == "1":
    blockTowerBruteForce(list_of_lists)
elif arg1 == "2":
    blockTowerDynamic(list_of_lists)
else:
    print("Choose an algorythm")