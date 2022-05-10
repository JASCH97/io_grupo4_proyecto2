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


def RotateBlockBrute(Block):

    for i in range(len(Block)):
            # Obtener un índice aleatorio
            randindex = random.randint(0, len(Block) - 1)
            # Intercambiar
            temp = Block[i]
            Block[i] = Block[randindex]
            Block[randindex] = temp

    return Block

def ValidateBlockBrute(Block):

    F = Block[0]
    P = Block[1]
    A = Block[2]

    if(F<=P):
        return True
    return False

#readInputFile()
#print(fileInformation)
#print(algorithmToUse)