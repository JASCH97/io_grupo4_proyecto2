from timeit import default_timer
from utilityFunctions import *


W=0
data=[]
Fmatriz=[]
inContainer=[] #save results of the dynamic method
inContainer2=()#save results of brute force method

#read the file
def readtext():
    global W,data
    readInputFile()
    W=fileInformation[0]
    data=fileInformation[1:]
    

"""
Function: matrix
Input: -
Output: -
Description: generates the necessary matrix filled with 0 
             to be able to work the dynamic method.
"""
def  matrix():
    for i in range(len(data)+1):
        a = [0]*(W+1)
        Fmatriz.append(a)
    print(len(data)+1)
        


"""
Function: bottomUpContainer
Input: -
Output: -
Description: iterates through the array filling it with the data from data .
"""
#data[i-1][0] = wi
#data[i-1][1] = bi

def bottomUpContainer():
    for i in range(1,len(Fmatriz)):
        
            for w in range(1,len(Fmatriz[0])):
                if data[i-1][0]>w:
                
                    Fmatriz[i][w]=Fmatriz[i-1][w]
                else:
                    if data[i-1][1] + Fmatriz[i-1][w-data[i-1][0]]>Fmatriz[i-1][w]:
                        Fmatriz[i][w]=data[i-1][1]+Fmatriz[i-1][w-data[i-1][0]]
                    else:
                        Fmatriz[i][w] = Fmatriz[i-1][w]


"""
Function:  findElementds
Input: -
Output: -
Description:traverse the matrix back to front
            getting the correct data and saving it in inContainer
"""

def findElementds():
    i = len(Fmatriz)-1
   
    k = len(Fmatriz[0])-1
  
    while i>0 and k>0 :
        if Fmatriz[i][k] != Fmatriz[i-1][k]:
            inContainer.append(i)
            k=k-data[i-1][0]
            i = i-1
            
        else:
            i = i-1
"""
Function:  finalresults
Input: -
Output: -
Description: prints the final results of the dynamic method

"""

def finalresults():
    maximumprofit = 0
    for i in list(inContainer):
        maximumprofit+= data[i-1][1]
    
    print("maximum benefit: ",maximumprofit)
    print("included: ", end="")

    for e in inContainer[:len(inContainer)-1]:
        print(e, end=", ")
    print(inContainer[len(inContainer)-1])

"""
Function:  BruteForceContainer
Input: -
Output: brute force result
Description: recursive method that obtains the maximum number of in brute force,
             in addition it is extracting which are the articles that were used to obtain that result

"""
def BruteForceContainer(W, data, n, inContainer2):
   
    if n == 0 or W == 0 :
       return 0,inContainer2
 
    if (data[n-1][0] > W):
        return BruteForceContainer(W, data, n-1, inContainer2)
   
    else:
        inContainer2Aux = (inContainer2 +(n,))
        temp,inContainer2Aux =  BruteForceContainer(W-data[n-1][0], data, n-1, (inContainer2Aux))
        temp+=data[n-1][1] 
        temp2,inContainer2 = BruteForceContainer(W, data, n-1, inContainer2)
        if temp>temp2:
            return temp,inContainer2Aux
        return temp2,inContainer2
  

"""
Function:  main
Input: -
Output: -
Description: it is to be able to use the functions described above,
             and show the results
""" 

def main() :
    readtext()
    x=algorithmToUse[0]
   
    if x == 1:
        print("brute force")
        n=len(data)
        w=W
        start = default_timer()
        finalresults2 = BruteForceContainer(w, data, n, inContainer2)
        #prints the final results of the brute force method
        print("maximum benefit: ", finalresults2[0])
        
        print("included: ", end="")
        for e in finalresults2[1][:len(finalresults2[1])-1]:
            print(e, end=", ")
        print(finalresults2[1][len(finalresults2[1])-1])
        end = default_timer()
        executionTime = end - start
        print("Execution Time: ",executionTime, "seconds\n")
    elif x == 2:
        print("dynamic")
        start = default_timer()
        matrix()
        bottomUpContainer()
        findElementds()
        finalresults()
        end = default_timer()
        executionTime = end - start
        print("Execution Time: ",executionTime, "seconds\n")
    else:
        print("wrong method entered: 1 brute force method, 2 dynamic method")

          
main()




 




