import sys
filename=open(sys.argv[1],"r")
qq=filename.readlines()
bulletList=[]
for costs in qq:
    element=costs.split(" ")
    count=0
    for string in element:
        count+=1
    for i in range(count):
        element[i]=float(element[i])
    bulletList.append(element)
ResultList=[]
forindex=[]
def calculateTotalCost(x):
    for j in range(len(x)):
        k=x[j]
        a=k[0]
        b=k[1]
        c=k[2]
        result=a+(a*c*10)+(b*10)
        if not result in ResultList:
            ResultList.append(result)
            forindex.append(result)
    return ResultList

def displayCosts(x):
    displayList=calculateTotalCost(x)
    for v in range(len(displayList)):
        print(str(v+1)+".house's total cost is",displayList[v])

def selectBestBuy(x):
    BestBuyList=calculateTotalCost(x)
    for index in range(1,len(BestBuyList)):
        currentvalue=BestBuyList[index]
        position=index
        while position>0 and BestBuyList[position-1]>currentvalue:
            BestBuyList[position]=BestBuyList[position-1]
            position=position-1
        BestBuyList[position]=currentvalue
    print("You should select",str(forindex.index(BestBuyList[0])+1)+"."+" house whose total cost is",str(BestBuyList[0])+".")
print("The total cost of each house :")
displayCosts(bulletList)
selectBestBuy(bulletList)

