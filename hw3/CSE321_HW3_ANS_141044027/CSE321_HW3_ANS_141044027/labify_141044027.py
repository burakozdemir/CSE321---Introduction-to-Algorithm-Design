import sys


graph = {1: set([2,3]),
    2: set([1,3,4]),
    3: set([1,2,4]),
    4: set([3,2]),
    5: set([6]),
    6: set([5]),
}

mapOfGTU = {1: set([2,3]),
            2: set([1,3]),
            3: set([1,2]),
}

def settolist(graph):
    mylistGraph = {}
    mylistGraph.update(graph)
    ###set to list
    for i in mylistGraph:
        if (i != 0):
            mylistGraph[i] = list(graph.get(i))
    return (mylistGraph)
def isHave(mylists,eleman):
    for i in mylists:
        if(i==eleman):
            return True
    return False
def myDFS(graphGtu,root):
    isaretli = []
    sira=[root]
    mygraph = settolist(graphGtu)
    while (sira):
        kose = sira.pop()
        ###icinde yoksa ekler ve genisletir
        if(not(isHave(isaretli,kose))):
            isaretli.append(kose)
            #print(mygraph[kose],isaretli ,set(mygraph[kose]) - set(isaretli) )
            sira.extend( list(set(mygraph[kose]) - set(isaretli)) )

    return isaretli ###isaretlileri return eder
def findMinimumCostToLabifyGTU(costLab,costRoad,graph):
    minCost = 0
    LabCost = 0
    RoadCost = 0
    listGraph = settolist(graph)
    mylist = []
    for i in graph:
        a=myDFS(graph,i)
        a.sort()
        if(not(isHave(mylist,a))):
            mylist.append(a)

    print(mylist)
    LabCost = len(mylist)*costLab

    for i in mylist:
        RoadCost+=(len(i)-1)*costRoad
    minCost=LabCost+RoadCost

    return (minCost)
minCost = findMinimumCostToLabifyGTU(5,2,graph)###complexicty analizi yap
print(minCost)# Output will be 18

