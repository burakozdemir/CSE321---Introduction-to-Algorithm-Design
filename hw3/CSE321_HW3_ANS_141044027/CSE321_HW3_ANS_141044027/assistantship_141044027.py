import sys
cartezyen = []

def beforeIndis(flag,onceki):
    if(flag[onceki]==0):
        return True
    else:
        return False
def findIndis(multArray,array):
    assistans = []
    ###
    nValue=len(multArray[0])
    index = len(array)
    while(index!=nValue):
        value = max(array)
        indis = array.index(value)
        del array[indis]
        index -= 1

    ###
    for i in multArray:
        assistans.append([])
    flag = []
    for i in range(0,len(array)):
        flag.append(0)
    flagIndex=0
    asstIndex=0
    for i in range(0,len(multArray)):
        tempflag=0
        for x in range(0,len(multArray[i])):
            if(flagIndex<len(array) and multArray[i][x]==array[flagIndex]):
                if(beforeIndis(flag,x)):
                    flag[x]=1
                    assistans[asstIndex]=x
                    flagIndex+=1
                    asstIndex+=1
                    tempflag=1
                    break
                else:
                    tempflag=1
        if(tempflag==0):
            assistans[asstIndex] = (-1)
            asstIndex += 1
    resultINdex=0
    for i in flag:
        if(i==1):
            resultINdex += 1
    if(resultINdex!=len(array)):
        return []
    else:
        return (assistans)
def generateOLasilik(Array,indis,myset,result):
    i = 0
    while (i<len(Array[myset])):
        indis[myset]=i
        if(myset==(len(Array)-1)):
            kartezyen = []
            for x in Array:
                kartezyen.append([])
            y = 0
            while(y<len(Array)):
                kartezyen[y]=(Array[y][indis[y]])
                y+=1
            result.append(kartezyen)
        else:
            generateOLasilik(Array,indis,myset+1,result)
        i+=1
def findToplam(arr):
    temp = 0
    for i in arr:
        temp += i
    return (temp)
def findOptimalAsistantship (inputTable):
    asst = []
    minTime = 0
    if(len(inputTable)<len(inputTable[0])):
        print("n value is bigger than r value")
        return(asst,minTime)
    index = 0
    ######olasılıklar kumelerı
    indis = []
    for i in inputTable:
        indis.append([])
    generateOLasilik(inputTable,indis,0,cartezyen)
    ######en kucuk kumeyı bulma
    minTime = 1000  ###temp value
    for i in cartezyen:
        tempasst= findIndis(inputTable,i)
        temp2=findToplam(i)
        if(minTime>=temp2 and len(tempasst)==len(inputTable)):
            minTime=temp2
            asst=tempasst
    for i in asst:
        if(i==(-1)):
            minTime+=6

    return (asst,minTime)

inputTable = [[5,8,7],[8,12,7],[4,8,5]]

asst, time = findOptimalAsistantship(inputTable)
print (asst)
print (time)
