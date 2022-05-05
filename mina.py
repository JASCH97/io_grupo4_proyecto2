from utilityFunctions import *
from timeit import default_timer
from colorama import init, Fore

#global variables
routes = []                         #All the paths
goldInAllRoutes = []                #gold recollected for each path


"""
Function: exhaustiveSearchAlgorithm
Input: matrixValues
Output: -
Description: This function performs an exhaustive search to try all 
             possible paths and also saves the gold that is collected on each path.
"""
def exhaustiveSearchAlgorithm(matrixValues):
    n = len(matrixValues) - 1
    m = len(matrixValues[0]) - 1
    
    i = 0

    while i <= n:

        goldCollected = matrixValues[i][0]
        routes.append(i)
        routes.append(0)

        if i == 0:

            #right path
            goldCollected = goldCollected + matrixValues[i][1]
            routes.append(i)
            routes.append(1)
            exhaustiveSearchAlgorithmAux(matrixValues,i,1,m,n,goldCollected)

            #diagonal down path
            goldCollected = matrixValues[i][0]        #gold reset
            routes.append(i)                          
            routes.append(0)

            goldCollected = goldCollected + matrixValues[i+1][1]
            routes.append(i+1)
            routes.append(1)
            exhaustiveSearchAlgorithmAux(matrixValues,i+1,1,m,n,goldCollected)

            i += 1

        elif i == n:
            #right path
            goldCollected = goldCollected + matrixValues[i][1]
            routes.append(i)
            routes.append(1)
            exhaustiveSearchAlgorithmAux(matrixValues,i,1,m,n,goldCollected)

            #diagonally up
            goldCollected = matrixValues[i][0]        #se resetea el oro
            routes.append(i)                           #se agregan de nuevo estos valores porque se tiene que
            routes.append(0)

            goldCollected = goldCollected + matrixValues[i-1][1]
            routes.append(i-1)
            routes.append(1)
            exhaustiveSearchAlgorithmAux(matrixValues,i-1,1,m,n,goldCollected)

            i += 1

        else:
            #right path
            goldCollected = goldCollected + matrixValues[i][1]
            routes.append(i)
            routes.append(1)
            exhaustiveSearchAlgorithmAux(matrixValues,i,1,m,n,goldCollected)

            #diagonal down path
            goldCollected = matrixValues[i][0]        #se resetea el oro
            routes.append(i)                           #se agregan de nuevo estos valores porque se tiene que
            routes.append(0)

            goldCollected = goldCollected + matrixValues[i+1][1]
            routes.append(i+1)
            routes.append(1)
            exhaustiveSearchAlgorithmAux(matrixValues,i+1,1,m,n,goldCollected)

            #diagonally up
            goldCollected = matrixValues[i][0]        #se resetea el oro
            routes.append(i)                           #se agregan de nuevo estos valores porque se tiene que
            routes.append(0)

            goldCollected = goldCollected + matrixValues[i-1][1]
            routes.append(i-1)
            routes.append(1)
            exhaustiveSearchAlgorithmAux(matrixValues,i-1,1,m,n,goldCollected)

            i += 1
        


"""
Function: exhaustiveSearchAlgorithmAux
Input: matrixValues, i, j, m, n, accumulatedGold
Output: -
Description: This function is auxiliary to exhaustiveSearchAlgorithm. Search for as much 
            gold as possible, given a point (i, j) , inside the mine
"""
def exhaustiveSearchAlgorithmAux(matrixValues,i,j,m,n,accumulatedGold):
    while j < m:
        
        #only can moves right or diagonal down
        if i == 0:         
            
            if(matrixValues[i][j+1] > matrixValues[i+1][j+1]):                      #if right > diagonal down
                accumulatedGold = accumulatedGold + matrixValues[i][j+1]
                routes.append(i)
                routes.append(j+1)
                j += 1
            
            else:                                                                   ##if right < diagonal down
                accumulatedGold = accumulatedGold + matrixValues[i+1][j+1]
                routes.append(i+1)
                routes.append(j+1)
                j += 1
                i += 1

        #only can moves right or diagonally up
        elif i == n:        

            if(matrixValues[i][j+1] > matrixValues[i-1][j+1]):                      #if right > diagonally up
                accumulatedGold = accumulatedGold + matrixValues[i][j+1]
                routes.append(i)
                routes.append(j+1)
                j += 1

            
            else:                                                                   #if right < diagonally up
                accumulatedGold = accumulatedGold + matrixValues[i-1][j+1]
                routes.append(i-1)
                routes.append(j+1)
                j += 1
                i -= 1

        #Can moves right, diagonally up or diagonal down
        elif i > 0 and i < n:                  

            if(matrixValues[i][j+1] > matrixValues[i+1][j+1] and matrixValues[i][j+1] > matrixValues[i-1][j+1]):    #if right > diagonal down and right > diagonally up
                accumulatedGold = accumulatedGold + matrixValues[i][j+1]
                routes.append(i)
                routes.append(j+1)
                j += 1
            
            elif(matrixValues[i-1][j+1] > matrixValues[i+1][j+1] and matrixValues[i-1][j+1] > matrixValues[i][j+1]):  #if diagonally up > right and diagonally up > diagonal down
                accumulatedGold = accumulatedGold + matrixValues[i-1][j+1]
                routes.append(i-1)
                routes.append(j+1)
                j += 1
                i -= 1
            
            else:                                                                   #if diagonal down > right and diagonal down > diagonally up
                accumulatedGold = accumulatedGold + matrixValues[i+1][j+1]
                routes.append(i+1)
                routes.append(j+1)
                j += 1
                i += 1

    goldInAllRoutes.append(accumulatedGold)                 #send the gold to the global variable


"""
Function: routesListToPathsMatrix
Input: numberOfCoordinates
Output: pathsMatrix
Description: This function transforms the list with the numbers of all the paths in an 
             ordered matrix according to the number of m elements
"""
def routesListToPathsMatrix(numberOfCoordinates):
    pathsMatrix = []

    while routes != []:

        pathsMatrix.append(routes[0:numberOfCoordinates])

        i = 0
        while i <= numberOfCoordinates - 1:
            routes.pop(0)
            i += 1
    
    return pathsMatrix
     
"""
Function: getOptimalPaths
Input: pathsMatrix, matrixValues
Output: optimalPaths
Description: This function takes the matrix of all the paths and finds which 
             one gets the maximum amount of gold
"""
def getOptimalPaths(pathsMatrix,matrixValues):
    optimalPaths = []
    maxGoldValue = max(goldInAllRoutes)
    
    for path in pathsMatrix:

        sumOfGold = calculateGoldFromAPath(path,matrixValues)

        if sumOfGold == maxGoldValue:
            optimalPaths.append(path)
    
    return optimalPaths

"""
Function: calculateGoldFromAPath
Input: path, matrixValues
Output: sumOfGold
Description: This function returns the amount of gold that is obtained given a path
"""
def calculateGoldFromAPath(path, matrixValues):

    i = 0
    sumOfGold = 0
    while i <= len(path) - 2:

        sumOfGold = sumOfGold + matrixValues[path[i]][path[i+1]]

        i += 2

    return sumOfGold

"""
Function: showFinalResults
Input: optimalPaths
Output: -
Description: This function takes the optimal routes and based on that prints 
             the result of the problem
"""
def showFinalResults(optimalPaths):

    print("\nMaximum amount of gold collected: ",max(goldInAllRoutes))
    print("Matrix coordinates leading to the result:")

    j = 0

    while j <= len(optimalPaths) - 1:
        i = 0
        k = 1
        while i <= len(optimalPaths[j]) - 2:

            print("%d) --> " %k + "( %d" %optimalPaths[j][i] ,", %d )" %optimalPaths[j][i+1])
            k += 1
            i += 2

        if j == len(optimalPaths) - 1:
            j += 1
        else:
            j += 1
            print("- - - OR - - -")

"""
Function: coloringOptimalPathsInMatrix
Input: matrixValues, optimalPaths
Output: -
Description: This function is responsible for coloring the optimal paths 
             found and printing them to the console.
"""
def coloringOptimalPathsInMatrix(matrixValues,optimalPaths):
    init()
    
    for path in optimalPaths:

        stringOptimalPaths = [[str(number) for number in row] for row in matrixValues]                      #reset str matrix in case there is more than 1 path

        while path != []:

            stringOptimalPaths[path[0]][path[1]] = Fore.GREEN + stringOptimalPaths[path[0]][path[1]]        #optimal path points are blue
            path.pop(0)
            path.pop(0)

        print("\nShowing the correct paths with colors: ")

        #list with green and white numbers from the matrix values 
        fullColorPath = []                                                                     
        for row in stringOptimalPaths:
            for number in row:

                #non optimal path points are white, there's an error if is not colored
                if number[0] != "\x1b":                                                              
                    newNumber = Fore.WHITE + number             
                    fullColorPath.append(newNumber)
                
                else:
                    fullColorPath.append(number)

        matrixColorPath = []                                    #

        #Matrix created that has elements colored in the same way as matrixValues
        for row in matrixValues:
            matrixColorPath.append([])
        
        m = len(matrixValues[0]) - 1
        i = 0
        while i <= len(matrixColorPath) - 1:
            j = 0
            while j <= m:
                matrixColorPath[i].append(fullColorPath[0])
                fullColorPath.pop(0)
                j += 1
            
            i += 1
        
        #the result is printed based on m elements
        m = len(matrixValues[0]) - 1            
        x = 0 
        while x <= m:                            
            print("   ".join('%s'%value for value in matrixColorPath[x]))
            x += 1

    #reset to white to avoid color errors in console
    print("\033[;37m")  
      


def main():
    readInputFile()

    #Exhaustive Search
    if algorithmToUse[0] == 1:                        
        start = default_timer()
        
        exhaustiveSearchAlgorithm(fileInformation)
        numberOfCoordinates = len(fileInformation[0]) * 2
        pathsMatrix = routesListToPathsMatrix(numberOfCoordinates)
        optimalPaths = getOptimalPaths(pathsMatrix, fileInformation)

        end = default_timer()
        executionTime = end - start
        showFinalResults(optimalPaths)
        coloringOptimalPathsInMatrix(fileInformation,optimalPaths)

        print("Execution Time: ",executionTime, "seconds\n")

main()