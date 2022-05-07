from timeit import default_timer


W=30
data=[[5,20],[15,50],[10,60],[10,62],[8,40]]
Fmatriz=[]
inContainer=[]
inContainer2=()
def  matrix():
    for i in range(len(data)+1):
        a = [0]*(W+1)
        Fmatriz.append(a)
        
#data[i-1][0] = wi
#data[i-1][1] = bi

def bottomUpContainer():
    for i in range(len(Fmatriz)):
        if i > 0:
            for w in range(len(Fmatriz[0])):
                if data[i-1][0]>w:
                
                    Fmatriz[i][w]=Fmatriz[i-1][w]
                else:
                    if data[i-1][1] + Fmatriz[i-1][w-data[i-1][0]]>Fmatriz[i-1][w]:
                        Fmatriz[i][w]=data[i-1][1]+Fmatriz[i-1][w-data[i-1][0]]
                    else:
                        Fmatriz[i][w] = Fmatriz[i-1][w]

def findElementds():
    i = len(Fmatriz)-1
   
    k = len(Fmatriz[0])-1
   
    while i!=0 and k!=0 :
        if Fmatriz[i][k] != Fmatriz[i-1][k]:
            inContainer.append(i)

            i = i-1
            k=k-data[i-1][0]
            if k<0:
                k=0
        else:
            i = i-1

def finalresults():
    maximumprofit = 0
    for i in list(inContainer):
        maximumprofit= maximumprofit + data[i-1][1]
    
    print("Beneficio máximo: ",maximumprofit)
    print("Incluidos: ", end="")

    for e in inContainer[:len(inContainer)-1]:
        print(e, end=", ")
    print(inContainer[len(inContainer)-1])


def BruteForceContainer(W, data, n, inContainer2):
   # initial conditions
    if n == 0 or W == 0 :
       return 0,inContainer2
   # If weight is higher than capacity then it is not included
    if (data[n-1][0] > W):
        return BruteForceContainer(W, data, n-1, inContainer2)
   # return either nth item being included or not
    else:
        inContainer2Aux = (inContainer2 +(n,))
        temp,inContainer2Aux =  BruteForceContainer(W-data[n-1][0], data, n-1, (inContainer2Aux))
        temp+=data[n-1][1] 
        temp2,inContainer2 = BruteForceContainer(W, data, n-1, inContainer2)
        if temp>temp2:
            return temp,inContainer2Aux
        return temp2,inContainer2
  
       

def main(x) :
    if x == 1:
        n=len(data)
        w=W
        start = default_timer()
        finalresults2 = BruteForceContainer(w, data, n, inContainer2)
        print("Beneficio máximo: ", finalresults2[0])
        
        print("Incluidos: ", end="")
        for e in finalresults2[1][:len(finalresults2[1])-1]:
            print(e, end=", ")
        print(finalresults2[1][len(finalresults2[1])-1])
        end = default_timer()
        executionTime = end - start
        print("Execution Time: ",executionTime, "seconds\n")
    else:
        start = default_timer()
        matrix()
        bottomUpContainer()
        findElementds()
        finalresults()
        end = default_timer()
        executionTime = end - start
        print("Execution Time: ",executionTime, "seconds\n")

          



main(1)


 




